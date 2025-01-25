# -*- coding: utf-8 -*-

try:
    import triton
except ImportError:
    raise ImportError(
        """Please install triton, you can install it with `pip install triton`
Or you can install if with `pip install rwkv-fla[cuda]`, `pip install rwkv-fla[xpu]`, `pip install rwkv-fla[rocm]`
For more information, please visit your Graphics Card's official website."""
    )

from rwkvfla.layers import (ABCAttention, Attention, BasedLinearAttention,
                        BitAttention, DeltaNet, GatedLinearAttention,
                        GatedSlotAttention, HGRN2Attention, HGRNAttention,
                        LinearAttention, MultiScaleRetention,
                        ReBasedLinearAttention)
from rwkvfla.models import (ABCForCausalLM, ABCModel, BitNetForCausalLM,
                        BitNetModel, DeltaNetForCausalLM, DeltaNetModel,
                        GLAForCausalLM, GLAModel, GSAForCausalLM, GSAModel,
                        HGRN2ForCausalLM, HGRN2Model, HGRNForCausalLM,
                        LinearAttentionForCausalLM, LinearAttentionModel,
                        RetNetForCausalLM, RetNetModel, RWKV6ForCausalLM,
                        RWKV6Model, TransformerForCausalLM, TransformerModel)

__all__ = [
    'ABCAttention',
    'Attention',
    'BasedLinearAttention',
    'BitAttention',
    'DeltaNet',
    'HGRNAttention',
    'HGRN2Attention',
    'GatedLinearAttention',
    'GatedSlotAttention',
    'LinearAttention',
    'MultiScaleRetention',
    'ReBasedLinearAttention',
    'ABCForCausalLM',
    'ABCModel',
    'BitNetForCausalLM',
    'BitNetModel',
    'DeltaNetForCausalLM',
    'DeltaNetModel',
    'HGRNForCausalLM',
    'HGRNModel',
    'HGRN2ForCausalLM',
    'HGRN2Model',
    'GLAForCausalLM',
    'GLAModel',
    'GSAForCausalLM',
    'GSAModel',
    'LinearAttentionForCausalLM',
    'LinearAttentionModel',
    'RetNetForCausalLM',
    'RetNetModel',
    'RWKV6ForCausalLM',
    'RWKV6Model',
    'TransformerForCausalLM',
    'TransformerModel',
    'chunk_gla',
    'chunk_retention',
    'fused_chunk_based',
    'fused_chunk_gla',
    'fused_chunk_retention'
]

__version__ = '0.1'
