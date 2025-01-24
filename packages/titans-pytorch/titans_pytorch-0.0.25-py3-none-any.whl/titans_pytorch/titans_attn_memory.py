from __future__ import annotations
import math
from functools import partial

import torch
from torch import nn, Tensor
import torch.nn.functional as F
from torch.nn import Linear, Module
from torch.func import functional_call, vmap, grad

from tensordict import TensorDict

from titans_pytorch.associative_scan import (
    associative_scan,
    binary_operator,
    pad_at_dim
)

import einx
from einops import rearrange, pack, unpack
from einops.layers.torch import Rearrange, Reduce

"""
ein notation:
b - batch
n - sequence
d - feature dimension
c - intra-chunk
"""

# constants

LinearNoBias = partial(Linear, bias = False)

# functions

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

def round_down_multiple(seq, mult):
    return seq // mult * mult

def round_up_multiple(seq, mult):
    return math.ceil(seq / mult) * mult

def pack_one_with_inverse(t, pattern):
    packed, packed_shape = pack([t], pattern)

    def inverse(out, inv_pattern = None):
        inv_pattern = default(inv_pattern, pattern)
        return unpack(out, packed_shape, inv_pattern)[0]

    return packed, inverse

# classes

# improvised attention as memory module
# todo - expand if see signal in experiments (update: not seeing it)

class MemoryAttention(Module):
    def __init__(
        self,
        dim
    ):
        super().__init__()
        self.weights = nn.ParameterList([
            nn.Parameter(torch.randn(dim, dim)), # queries
            nn.Parameter(torch.randn(dim, dim)), # keys
            nn.Parameter(torch.randn(dim, dim)), # values weight 1
            nn.Parameter(torch.randn(dim, dim)), # values weight 2
        ])

    def forward(self, x):

        assert x.shape[-2] > 1, 'chunk size needs to be greater than 1 for using attention as memory'

        wq, wk, wv1, wv2 = self.weights

        q = x @ wq
        k = x @ wk
        v = x @ wv1

        hidden = F.scaled_dot_product_attention(
            q, k, v,
            is_causal = True
        )

        return F.silu(hidden) @ wv2

# main neural memory

def default_loss_fn(pred, target):
    return (pred - target).pow(2).mean(dim = -1).sum()

class NeuralMemory(Module):
    def __init__(
        self,
        dim,
        chunk_size = 1,
        dim_head = None,
        heads = 1,
        model: MemoryAttention | None = None,
        store_memory_loss_fn: Callable = default_loss_fn,
        pre_rmsnorm = True,
        post_rmsnorm = True,
        use_accelerated_scan = False,
        default_model_kwargs: dict = dict()
    ):
        super().__init__()

        # norms

        self.retrieve_norm = nn.RMSNorm(dim) if pre_rmsnorm else nn.Identity()
        self.store_norm = nn.RMSNorm(dim) if pre_rmsnorm else nn.Identity()

        self.post_rmsnorm = nn.RMSNorm(dim) if post_rmsnorm else nn.Identity()

        # maybe multi-headed

        dim_head = default(dim_head, dim)
        dim_inner = dim_head * heads

        self.split_heads = Rearrange('b n (h d) -> (b h) n d', h = heads)
        self.merge_heads = Rearrange('(b h) n d -> b n (h d)', h = heads)
        self.combine_heads = LinearNoBias(dim_inner, dim) if heads > 1 else nn.Identity()

        # memory mlp

        if not exists(model):
            model = MemoryAttention(dim_head, **default_model_kwargs)

        assert not exists(next(model.buffers(), None)), 'model cannot have buffers for now'

        # the memory is the weights of the model

        self.memory_model = model

        # the chunk size within the paper where adaptive step, momentum, weight decay are shared

        self.chunk_size = chunk_size

        # prepare function for per sample gradients from model above, using torch.func

        def forward_and_loss(params, inputs, target):
            pred = functional_call(self.memory_model, params, inputs)
            loss = self.store_memory_loss_fn(pred, target) # simple mse loss in paper - eq (12) - |M(k) - v|²
            return loss

        self.per_sample_grad_fn = vmap(grad(forward_and_loss), in_dims = (None, 0, 0))

        # queries for retrieving from the model

        self.to_queries = LinearNoBias(dim, dim_inner)

        # keys and values for storing to the model

        self.to_keys_values = LinearNoBias(dim, dim_inner * 2)
        self.store_memory_loss_fn = store_memory_loss_fn

        # learned adaptive learning rate and momentum
        # todo - explore mlp layerwise learned lr / momentum

        self.to_momentum = nn.Sequential(
            Reduce('b (n c) ... -> b n ...', 'mean', c = chunk_size),
            LinearNoBias(dim, heads),
            Rearrange('b n h -> (b h) n 1')
        )

        self.to_adaptive_step = nn.Sequential(
            Reduce('b (n c) ... -> b n ...', 'mean', c = chunk_size),
            LinearNoBias(dim, heads),
            Rearrange('b n h -> (b h) n')
        )

        # weight decay factor

        self.to_decay_factor = nn.Sequential(
            Reduce('b (n c) ... -> b n ...', 'mean', c = chunk_size),
            LinearNoBias(dim, heads),
            Rearrange('b n h -> (b h) n 1')
        )

        # maybe use accelerated scan

        self.use_accelerated_scan = use_accelerated_scan

    def init_weights_and_momentum(self):
        params = TensorDict(dict(self.memory_model.named_parameters()))

        init_weights = params.clone().zero_()
        init_momentum = params.clone().zero_()

        return init_weights, init_momentum

    def store_memories(
        self,
        seq,
        past_state: tuple[dict[str, Tensor], dict[str, Tensor]]
    ):

        seq = self.store_norm(seq)

        # curtail sequence by multiple of the chunk size
        # only a complete chunk of the sequence provides the memory for the next chunk

        seq_len, chunk_size = seq.shape[-2], self.chunk_size
        round_down_seq_len = round_down_multiple(seq_len, self.chunk_size)

        seq = seq[:, :round_down_seq_len]

        # curr weights + past weights, in the case that the initial weights are learned

        curr_weights = TensorDict(dict(self.memory_model.named_parameters()))

        past_state = tuple(TensorDict(d) for d in past_state)
        past_weights, past_momentum = past_state

        curr_weights = curr_weights + past_weights

        # pack batch and sequence dimension

        adaptive_lr = (self.to_adaptive_step(seq).sigmoid() * -15).exp() # from 1. - 1e-7

        adaptive_momentum = self.to_momentum(seq).sigmoid()
        decay_factor = self.to_decay_factor(seq).sigmoid()

        # keys and values

        keys, values = self.to_keys_values(seq).chunk(2, dim = -1)

        # maybe multi head

        keys, values = map(self.split_heads, (keys, values))

        batch = keys.shape[0]

        # take care of chunking

        keys, values = tuple(rearrange(t, 'b (n c) d -> (b n) c d', c = self.chunk_size) for t in (keys, values))

        # get grads and extra auxiliary loss (for backwarding through qkv projection in base neural memory module)

        grads = self.per_sample_grad_fn(dict(curr_weights), keys, values)

        grads = TensorDict(grads)

        # restore batch and sequence dimension

        grads = grads.apply(lambda t: rearrange(t, '(b n) ... -> b n ...', b = batch))

        # multiply gradients with learned adaptive step size

        surprises = grads.apply(lambda t: einx.multiply('b n ..., b n -> b n ...', t, -adaptive_lr))

        # determine scan function

        def default_associative_scan(gates, inputs):
            _, outputs = associative_scan(binary_operator, (gates, inputs))
            return outputs

        if self.use_accelerated_scan:
            from accelerated_scan.triton import scan as triton_scan
            from accelerated_scan.warp import scan as warp_scan

            scan = triton_scan if seq.is_cuda else warp_scan

            def accelerate_scan_fn(gates, inputs):
                gates = gates.expand_as(inputs)
                gates, inputs = tuple(rearrange(t, 'b n d -> b d n') for t in (gates, inputs))

                seq_len = gates.shape[-1]
                next_power_two_seq_len = 2 ** max(5, int(math.ceil(math.log2(seq_len))))

                gates = F.pad(gates, (0, next_power_two_seq_len - seq_len))
                inputs = F.pad(inputs, (0, next_power_two_seq_len - seq_len))

                outputs = scan(gates, inputs)

                outputs = outputs[..., :seq_len]
                outputs = rearrange(outputs, 'b d n -> b n d')
                return outputs

            scan_fn = accelerate_scan_fn
        else:
            scan_fn = default_associative_scan

        # momentum + weight decay - momentum is the new contribution, as most linear RNNs have learned forgetting gates

        next_momentum = TensorDict()
        updates = TensorDict()

        for param_name, surprise in surprises.items():

            surprise, inverse_pack = pack_one_with_inverse(surprise, 'b n *')

            # derive momentum with associative scan - eq (10)

            momentum = scan_fn(adaptive_momentum, surprise) # momentum is S / surprise in the paper

            # use associative scan again for learned forgetting (weight decay) - eq (13)

            update = scan_fn(1. - decay_factor, momentum) # momentum is S / surprise in the paper

            updates[param_name] = inverse_pack(update)
            next_momentum[param_name] = inverse_pack(momentum)

        # compute the next weight per batch

        last_update = updates.apply(lambda t: t[:, -1])

        next_state = (curr_weights + last_update, next_momentum)

        return updates, next_state

    def retrieve_memories(
        self,
        seq,
        past_weights: dict[str, Tensor] | None = None,
    ):
        chunk_size = self.chunk_size
        seq_len = seq.shape[1]

        seq = self.retrieve_norm(seq)

        assert seq_len > chunk_size

        seq = seq[:, chunk_size:]
        curtailed_seq_len = seq.shape[-2]

        next_seq_len = round_up_multiple(curtailed_seq_len + 1, chunk_size)

        padding = next_seq_len - curtailed_seq_len

        seq = pad_at_dim(seq, (0, padding), dim = 1)

        # the parameters of the memory model stores the memories of the key / values
        # when the MLP has only 1 weight matrix, it is equivalent to `kv` fast weight memories from linear attention literature (recall fetching of memories is q @ (kv)) / schmidhuber's paper

        curr_weights = TensorDict(dict(self.memory_model.named_parameters()))

        if exists(past_weights):
            past_weights = TensorDict(past_weights)
            assert past_weights.keys() == curr_weights.keys()

            curr_weights = curr_weights + past_weights

        # sequence Float['b n d'] to queries

        queries = self.to_queries(seq)

        # maybe multihead

        queries = self.split_heads(queries)

        batch = queries.shape[0]

        # fetch values from memory model

        curr_weights = curr_weights.apply(lambda t: rearrange(t, 'b n ... -> (b n) ...'))
        queries = rearrange(queries, 'b (n c) d -> (b n) c d', c = chunk_size)

        # forward functional call

        values = functional_call(self.memory_model, dict(curr_weights), queries)

        # reconstitute batch dimension

        values = rearrange(values, '(b n) c d -> b (n c) d', b = batch)

        # maybe merge heads and combine

        values = self.merge_heads(values)

        values = self.combine_heads(values)

        # post norm, somehow could not stabilize this without it, not in paper

        values = self.post_rmsnorm(values)

        # restore

        values = pad_at_dim(values, (chunk_size, 0), dim = 1, value = 0.) # todo, used a learned null memory embedding instead of 0s for retrieving from empty neural memory
        values = values[:, :-padding]

        return values

    def forward(
        self,
        seq,
        store_seq = None,
        past_state: tuple[dict[str, Tensor], dict[str, Tensor]] | None = None,
        return_next_memories = False
    ):
        batch, seq_len = seq.shape[:2]

        if seq_len <= self.chunk_size:
            return torch.zeros_like(seq)

        if exists(past_state):
            past_state = tuple(TensorDict(d) for d in past_state)

        if not exists(past_state):
            past_state = self.init_weights_and_momentum()

        store_seq = default(store_seq, seq)

        updates, next_memories = self.store_memories(store_seq, past_state)

        past_weights, _ = past_state

        retrieved = self.retrieve_memories(seq, past_weights + updates)

        if not return_next_memories:
            return retrieved

        return retrieved, next_memories
