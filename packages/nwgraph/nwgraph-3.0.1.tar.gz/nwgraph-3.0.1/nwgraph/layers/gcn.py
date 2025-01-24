"""GCN layer"""
from overrides import overrides
import torch as tr
from torch import nn

from nwgraph import Graph
from nwgraph.message_passing import TensorMessagePassing, MessagePassingType, NodeStatesType

class GCN(TensorMessagePassing):
    """
    Graph Convolutional Network a-la https://tkipf.github.io/graph-convolutional-networks/

    Parameters:
    - graph The graph we operate on
    - in_features The number of input features for each node
    - out_features The number of output features for each node

    """
    def __init__(self, graph: Graph, in_features: int, out_features: int, store_messages: bool = False):
        super().__init__(graph, store_messages)
        self.W = nn.Linear(in_features, out_features, bias=True)
        self.A = graph.adjacency_matrix
        self.A_self_loop = tr.eye(len(self.A)) + self.A # pylint: disable=invalid-name
        self.D = self.A_self_loop.sum(dim=1, keepdim=True)

    @overrides
    def message_pass(self) -> MessagePassingType:
        h = self.graph.node_states
        y = self.W(self.A_self_loop.to(self.device) @ h)
        return y

    @overrides
    def aggregate(self, messages: MessagePassingType) -> NodeStatesType:
        return messages / self.D.to(self.device)

    @overrides
    def update(self, aggregation: NodeStatesType) -> NodeStatesType:
        return aggregation
