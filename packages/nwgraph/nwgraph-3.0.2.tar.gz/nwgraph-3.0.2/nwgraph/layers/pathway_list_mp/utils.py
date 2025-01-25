"""utils functions for pathway_list_mp implementation"""
from typing import Callable
import torch as tr
from torch import nn
from nwgraph.pathway import Pathway

# nn.Linear (type/callable) or nn.Linear(1, 3) (instantiated)
ModelOrLazyModel = Callable[[int, int], nn.Module] | nn.Module
# 1 model per entire mp layer or 1 per edge
MpModels = ModelOrLazyModel | list[ModelOrLazyModel]
EnsembleFn = Callable[[tr.Tensor], tr.Tensor]  # a single new_state = f([node_msgs])
EnsembleType = dict | str | EnsembleFn | list  # 'mean' or a lambda function; list if we provide one per timestamp
AggFnsType = nn.ModuleDict  # dict[int, dict[str, EnsembleType]]


class MeanEnsemble(nn.Module):
    """MeanEnsemble"""
    # pylint: disable=unused-argument
    def forward(self, votes: tr.Tensor, voters: list[Pathway]):
        """fwd fn"""
        return votes.mean(dim=0)

class MedianEnsemble(nn.Module):
    """MedianEnsemble"""
    # pylint: disable=unused-argument
    def forward(self, votes: tr.Tensor, voters: list[Pathway]):
        """fwd fn"""
        return votes.median(dim=0).values

class SumEnsemble(nn.Module):
    """SumEnsemble"""
    # pylint: disable=unused-argument
    def forward(self, votes: tr.Tensor, voters: list[Pathway]):
        """fwd fn"""
        return votes.sum(dim=0)
