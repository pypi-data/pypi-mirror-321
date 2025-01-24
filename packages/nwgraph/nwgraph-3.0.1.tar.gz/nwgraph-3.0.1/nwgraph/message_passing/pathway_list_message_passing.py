"""
PathwayListMessagePassing module. States and all 3 methods receive and return a Dict of list of tensors. This is based
on the old nwgraph/ngclib implementation. Each edge has its own set of weights and the 3 functions: message_pass,
aggregate, update, are called for each pathway's last edge separately.
"""

from abc import abstractmethod, ABC
from typing import Mapping, Any
from overrides import overrides
from torch import nn

from .message_passing import MessagePassing, MessagePassingType, NodeStatesType
from ..graph import Graph
from ..pathway import PathwayList
from ..utils import parsed_str_type

class PathwayListMessagePassing(MessagePassing, ABC):
    """
    DictMessagePassing abstract class. Adds `pathway_list_models` and operates on Graphs.
    In total, we have 4 methods to implement: `message_pass`, `aggregate`, `update` and `pathway_list_models`.
    """

    def __init__(self, graph: Graph, pathways: PathwayList, store_messages: bool = False):
        super().__init__(graph, store_messages=store_messages)
        assert isinstance(pathways, PathwayList), pathways
        self.pathways = pathways

    @property
    @abstractmethod
    def pathway_list_models(self) -> dict[str, dict[str, nn.Module]]:
        """The models of each edge in this message passing module"""

    @abstractmethod
    def message_pass(self) -> MessagePassingType:
        """Method that defines how messages are sent in one iteration."""

    @abstractmethod
    def aggregate(self, messages: MessagePassingType) -> NodeStatesType:
        """
        Aggregation function that must transform all the received messages of a node to one message after each
        iteration has finished. Basically f(node, [message]) = (node, message).
        """

    @abstractmethod
    def update(self, aggregation: NodeStatesType) -> NodeStatesType:
        """Update function that updates the nodes' representation at the end of each iteration"""

    @property
    def n_steps(self) -> int:
        """returns the number of steps of this mp_layer"""
        return self.pathways.n_steps

    @property
    @overrides(check_signature=False)
    def node_states(self) -> NodeStatesType:
        return self.graph.node_states

    @node_states.setter
    def node_states(self, node_states: NodeStatesType):
        self.graph.node_states = node_states
        self.graph.n_nodes_set = len(self.graph.node_states)

    @overrides(check_signature=False)
    def forward(self, x: MessagePassingType) -> Graph:
        return super().forward(x) # type: ignore

    @overrides
    def state_dict(self, *args, destination=None, prefix="", keep_vars=False):
        """
        we need to override here because some layers may define other views of the graph at constructor time and
        torch will track these views separately leading to too many items in the dictionary
        """
        models: nn.ModuleDict = self.pathway_list_models
        return models.state_dict(*args, destination=destination, prefix=prefix, keep_vars=keep_vars)

    @overrides
    def load_state_dict(self, state_dict: Mapping[str, Any], strict: bool=True, assign: bool=False):
        """Calls load_state_dict on the models"""
        models: nn.ModuleDict = self.pathway_list_models
        return models.load_state_dict(state_dict, strict=strict, assign=assign)

    def __str__(self) -> str:
        n_path_edges = len([x for x in self.pathways.partial_pathways if x.has_output_edge()])
        return f"Layer: '{parsed_str_type(self)}' (paths: {len(self.pathways)}, path edges: {n_path_edges}, " \
               f"n_steps: {self.pathways.n_steps}, memory: {self.is_memory_populated()}) on G: {self.graph}"

    def __repr__(self) -> str:
        # this is a separate method so we can call repr() for pathways which has colors for easier debugging
        n_path_edges = len([x for x in self.pathways.partial_pathways if x.has_output_edge()])
        return f"Layer: '{parsed_str_type(self)}' (paths: {len(self.pathways)}, path edges: {n_path_edges}, " \
               f"n_steps: {self.pathways.n_steps}, memory: {self.is_memory_populated()}) on G: {repr(self.graph)}"
