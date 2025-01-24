from __future__ import annotations
from math import ceil
from functools import partial

import torch
from torch import nn, cat
import torch.nn.functional as F
from torch.nn import Module, ModuleList, Linear

from einops import repeat, rearrange, pack, unpack
from einops.layers.torch import Rearrange

from hyper_connections import get_init_and_expand_reduce_stream_functions

# absolute and relative positions

from axial_positional_embedding import ContinuousAxialPositionalEmbedding
from rotary_embedding_torch import RotaryEmbedding

# proposed neural memory

from titans_pytorch.titans import NeuralMemory

# constants

LinearNoBias = partial(Linear, bias = False)

# helpers

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

def identity(t):
    return t

def round_up_multiple(seq, mult):
    return ceil(seq / mult) * mult

def pad_and_segment_with_inverse(seq, segment_len):
    batch, seq_len = seq.shape[:2]

    need_segment = seq_len >= segment_len

    if not need_segment:
        return seq, identity

    next_seq_len_mult = round_up_multiple(seq_len, segment_len)

    padding = next_seq_len_mult - seq_len
    needs_pad = padding > 0

    if needs_pad:
        seq = F.pad(seq, (0, 0, 0, padding))

    seq = rearrange(seq, 'b (w n) d -> (b w) n d', n = segment_len)

    def inverse(out):
        out = rearrange(out, '(b w) n d -> b (w n) d', b = batch)

        if needs_pad:
            out = out[:, :-padding]

        return out

    return seq, inverse

# feedforward and attention

class GEGLU(Module):
    def forward(self, x):
        x, gate = x.chunk(2, dim = -1)
        return F.silu(gate) * x

def FeedForward(dim, mult = 4):
    dim_inner = int(dim * mult * 2 / 3)

    return nn.Sequential(
        nn.RMSNorm(dim),
        nn.Linear(dim, dim_inner * 2),
        GEGLU(),
        nn.Linear(dim_inner, dim)
    )

class SegmentedAttention(Module):
    def __init__(
        self,
        dim,
        segment_len,
        num_persist_mem_tokens = 0,
        num_longterm_mem_tokens = 0,
        dim_head = 64,
        heads = 8,
    ):
        super().__init__()
        self.norm = nn.RMSNorm(dim)

        dim_inner = dim_head * heads

        self.rotary_emb = RotaryEmbedding(dim_head)

        self.to_qkv = LinearNoBias(dim, dim_inner * 3)
        self.to_out = LinearNoBias(dim_inner, dim)

        self.segment_len = segment_len
        self.num_longterm_mem_tokens = num_longterm_mem_tokens

        total_segment_len = segment_len + num_longterm_mem_tokens

        self.split_heads = Rearrange('b n (h d) -> b h n d', h = heads)
        self.merge_heads = Rearrange('b h n d -> b n (h d)')

        self.persistent_memory = nn.Parameter(torch.zeros(2, heads, num_persist_mem_tokens, dim_head))

    def forward(self, seq):
        segment_len, num_longterm_mem_tokens = self.segment_len, self.num_longterm_mem_tokens
        total_segment_len = segment_len + num_longterm_mem_tokens

        batch, seq_len = seq.shape[:2]

        # auto pad to multiple
        # todo - get rid of logic with flex attention

        seq, inverse_segment = pad_and_segment_with_inverse(seq, total_segment_len)

        # attention

        seq = self.norm(seq)

        q, k, v = self.to_qkv(seq).chunk(3, dim = -1)
        q, k, v = map(self.split_heads, (q, k, v))

        # take care of persistent memory key / values

        pmk, pmv = tuple(repeat(t, 'h n d -> b h n d', b = seq.shape[0]) for t in self.persistent_memory)

        # relative positions

        q, k = self.rotary_emb.rotate_queries_with_cached_keys(q, k)

        # persistent memory

        k = cat((pmk, k), dim = -2)
        v = cat((pmv, v), dim = -2)

        # sdpa

        out = F.scaled_dot_product_attention(q, k, v, is_causal = True)

        out = self.merge_heads(out)

        out = self.to_out(out)

        out = inverse_segment(out)

        return out

# MAC transformer

class MemoryAsContextTransformer(Module):
    def __init__(
        self,
        *,
        num_tokens,
        dim,
        depth,
        segment_len,
        num_longterm_mem_tokens = 0,
        num_persist_mem_tokens = 0,
        dim_head = 64,
        heads = 8,
        ff_mult = 4,
        num_residual_streams = 4,
        neural_memory_kwargs: dict = dict(),
        neural_memory_layers: tuple[int, ...] | None = None,
    ):
        super().__init__()

        self.token_emb = nn.Embedding(num_tokens, dim)

        self.axial_pos_emb = ContinuousAxialPositionalEmbedding(dim = dim, num_axial_dims = 2)

        # long term mem tokens

        self.segment_len = segment_len

        self.num_longterm_mem_tokens = num_longterm_mem_tokens
        has_longterm_mems = num_longterm_mem_tokens > 0

        self.longterm_mems = nn.Parameter(torch.randn(num_longterm_mem_tokens, dim) * 0.02)

        # hyper conection

        init_hyper_conn, self.expand_streams, self.reduce_streams = get_init_and_expand_reduce_stream_functions(num_residual_streams, disable = num_residual_streams == 1)

        self.layers = ModuleList([])
        self.neural_mem_layers = ModuleList([])

        layers = tuple(range(1, depth + 1))

        if not exists(neural_memory_layers):
            neural_memory_layers = layers if has_longterm_mems else ()

        assert not (num_longterm_mem_tokens > 0 and len(neural_memory_layers) == 0), 'empty `neural_memory_layers` when longterm memory tokens are present'

        for layer in layers:

            # neural memory

            mem = None

            if layer in neural_memory_layers:
                assert has_longterm_mems, '`num_longterm_mem_tokens` must be greater than 0'

                mem = NeuralMemory(
                    dim = dim,
                    chunk_size = num_longterm_mem_tokens + segment_len,
                    **neural_memory_kwargs
                )

                mem = init_hyper_conn(dim = dim, branch = mem)

            self.neural_mem_layers.append(mem)

            # attention and feedforward

            attn = SegmentedAttention(
                dim = dim,
                dim_head = dim_head,
                heads = heads,
                segment_len = segment_len,
                num_longterm_mem_tokens = num_longterm_mem_tokens,
                num_persist_mem_tokens = num_persist_mem_tokens
            )

            ff = FeedForward(dim = dim, mult = ff_mult)

            self.layers.append(ModuleList([
                init_hyper_conn(dim = dim, branch = attn),
                init_hyper_conn(dim = dim, branch = ff)
            ]))

        self.norm = nn.RMSNorm(dim)

        self.to_logits = LinearNoBias(dim, num_tokens)

    def forward(
        self,
        x,
        return_loss = False
    ):

        if return_loss:
            x, labels = x[:, :-1], x[:, 1:]

        # math

        batch, seq_len, segment_len, num_longterm_mem_tokens= *x.shape, self.segment_len, self.num_longterm_mem_tokens

        windows = ceil(seq_len / segment_len)
        total_segment_len = segment_len + num_longterm_mem_tokens

        # token embedding

        x = self.token_emb(x)

        # intersperse longterm memory

        x, inverse_segment = pad_and_segment_with_inverse(x, segment_len)

        mems = repeat(self.longterm_mems, 'n d -> b n d', b = x.shape[0])
        x, mem_ps = pack((x, mems), 'b * d')

        x = inverse_segment(x)

        # apply axial positional embedding
        # so intra and inter segment can be more easily discerned by the network

        pos_emb = self.axial_pos_emb((windows, total_segment_len), flatten = True)
        x = x + pos_emb[:x.shape[-2]]

        # expand and reduce streams for hyper connections

        x = self.expand_streams(x)

        for (attn, ff), maybe_neural_mem in zip(self.layers, self.neural_mem_layers):

            if exists(maybe_neural_mem):
                mems = maybe_neural_mem(mems)

            x = attn(x)

            x = ff(x)

        x = self.reduce_streams(x)

        # excise out the memories

        x, inverse_segment = pad_and_segment_with_inverse(x, total_segment_len)

        x, mem = unpack(x, mem_ps, 'b * d')

        x = inverse_segment(x)

        # to logits

        x = self.norm(x)

        logits = self.to_logits(x)

        if not return_loss:
            return logits

        return F.cross_entropy(rearrange(logits, 'b n l -> b l n'), labels)
