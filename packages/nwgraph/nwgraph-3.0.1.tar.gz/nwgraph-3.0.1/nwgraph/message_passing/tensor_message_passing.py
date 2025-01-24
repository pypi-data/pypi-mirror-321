"""
TensorMessagePassing module. states and all 3 methods receive and return a Tensor. This is identical to torchgeometric
and is built for compatibility with GCN-style MessagePassing modules.
"""
from abc import ABC
from overrides import overrides
import torch as tr

from .message_passing import MessagePassing

class TensorMessagePassing(MessagePassing, ABC):
    """TensorMessagePassing implementation"""
    @property
    @overrides
    def node_states(self) -> tr.Tensor:
        """The node states of this message passing module"""
        return self.graph.node_states

    @node_states.setter
    def node_states(self, node_states: tr.Tensor):
        """message passing setter for this module. We need items to be torch tensors by default."""
        assert isinstance(node_states, tr.Tensor), type(node_states)
        assert len(node_states) == len(self.graph.nodes), (len(node_states), len(self.graph.nodes))
        self.graph.node_states = node_states
        self.graph.n_nodes_set = \
            (~tr.isnan(self.node_states).reshape((len(self.graph.nodes), -1)).sum(dim=1).type(tr.bool)).sum().item()
