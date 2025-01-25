"""
PathwayListMessagePassing module. States and all 3 methods receive and return a Dict of list of tensors. This is based
on the old nwgraph/ngclib implementation. Each edge has its own set of weights and the 3 functions: message_pass,
aggregate, update, are called for each pathway's last edge separately.
"""

from abc import ABC
from overrides import overrides

from .message_passing import MessagePassing, MessagePassingType
from ..graph import Graph
from ..pathway import PathwayList
from ..utils import parsed_str_type

class PathwayListMessagePassing(MessagePassing, ABC):
    """
    DictMessagePassing abstract class. Adds `pathway_list_models` and operates on Graphs.
    In total, we have 4 methods to implement: `message_pass`, `aggregate`, `update`.
    """

    def __init__(self, graph: Graph, pathways: PathwayList, store_messages: bool = False):
        super().__init__(graph, store_messages=store_messages)
        assert isinstance(pathways, PathwayList), pathways
        self.pathways = pathways

    @property
    def n_steps(self) -> int:
        """returns the number of steps of this mp_layer"""
        return self.pathways.n_steps

    @overrides(check_signature=False)
    def forward(self, x: MessagePassingType) -> Graph:
        return super().forward(x) # type: ignore

    def __str__(self) -> str:
        n_path_edges = len([x for x in self.pathways.partial_pathways if x.has_output_edge()])
        return f"Layer: '{parsed_str_type(self)}' (paths: {len(self.pathways)}, path edges: {n_path_edges}, " \
               f"n_steps: {self.n_steps}, memory: {self.is_memory_populated()}) on G: {self.graph}"

    def __repr__(self) -> str:
        # this is a separate method so we can call repr() for pathways which has colors for easier debugging
        n_path_edges = len([x for x in self.pathways.partial_pathways if x.has_output_edge()])
        return f"Layer: '{parsed_str_type(self)}' (paths: {len(self.pathways)}, path edges: {n_path_edges}, " \
               f"n_steps: {self.n_steps}, memory: {self.is_memory_populated()}) on G: {repr(self.graph)}"
