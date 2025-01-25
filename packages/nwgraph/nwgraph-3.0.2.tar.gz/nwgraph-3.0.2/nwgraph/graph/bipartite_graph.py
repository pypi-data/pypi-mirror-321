"""Bipartite graph module"""
from __future__ import annotations
from typing import Type
from overrides import overrides

from .graph import Graph
from ..utils import parsed_str_type, EdgeIndex, NodeArgs
from ..logger import nwg_logger as logger
from .node import Node


class BipartiteGraph(Graph):
    """
    BipartiteGraph class. Extends graph by providing nodes of types a and b (2 partitions)

    Parameters:
    - edge_indexes: The list of nodes pairs used for edges. Can be indexes or strings. If strings, we must also provide
    the node names.
    - n_nodes: The number of nodes. If not provided, it's infered from edge_indexes.
    - edge_types: The type of edges. Used to instantiate the edges. If not provided, defaults to `nwgraph.Edge`.
    - node_names: The node names. If not provided, it'll default to integer names based on edge_indexes. Must be
    provided if edge_indexes is based on node names (strings).
    - node_types: The type of nodes. Used to instantiate the nodes. IF not provided, defaults to `nwgraph.Node`.
    - node_args: The arguments of each node. If `node_types` has a different constructor than `nwgraph.Node(name: str)`
    , this dictionary must be provided.
    - nodes_type_a: A list of strings, representing the names of the nodes of type a. Nodes of type b are inferred.
    """
    def __init__(self, *args, nodes_type_a: list[str], **kwargs):
        super().__init__(*args, **kwargs)
        self._nodes_type_a, self._nodes_type_b = self._build_nodes(nodes_type_a)

    @property
    def nodes_type_a(self) -> list[Node]:
        """The list of input nodes"""
        return self._nodes_type_a

    @property
    def nodes_type_b(self) -> list[Node]:
        """The list of output nodes"""
        return self._nodes_type_b

    def clone(self) -> BipartiteGraph:
        return type(self)(edge_indexes=self.edge_indexes, n_nodes=len(self.nodes), edge_types=self.edge_types,
                          node_names=self.node_names, node_types=self.node_types, node_args=self.node_args,
                          nodes_type_a=[n for n in self.nodes_type_a if n in self.nodes])

    @overrides
    # pylint: disable=protected-access
    def subgraph(self, edge_names_or_indexes: list[str] | list[EdgeIndex], prune_nodes: bool = False) -> Graph:
        res: BipartiteGraph = super().subgraph(edge_names_or_indexes, prune_nodes=prune_nodes)
        if prune_nodes:
            res._nodes_type_a = [node for node in self._nodes_type_a if node in res.nodes]
            res._nodes_type_b = [node for node in self._nodes_type_b if node in res.nodes]
        return res

    @overrides
    def add_nodes(self, node_names: list[str] | list[int], node_types: list[Type[Node]], node_args: list[NodeArgs]):
        super().add_nodes(node_names, node_types, node_args)
        logger.debug(f"Adding {node_names} to nodes_type_b as well.")
        self._nodes_type_b.extend([self.name_to_node[n] for n in node_names])

    @overrides
    def remove_nodes(self, node_names: list[str] | list[int]):
        super().remove_nodes(node_names)
        logger.debug(f"Removing {node_names} from nodes_type_b as well.")
        self._nodes_type_b = [node for node in self.nodes_type_b if node not in node_names]
        self._nodes_type_a = [node for node in self.nodes_type_a if node not in node_names]

    # Private methods
    def _build_nodes(self, nodes_type_a: list[str]) -> tuple[list[Node], list[Node]]:
        assert set(nodes_type_a).issubset(self.node_names), f"Type a: {nodes_type_a}. All nodes: {self.node_names}"
        nodes_type_a = [self.name_to_node[n] for n in nodes_type_a]
        nodes_type_b = [self.name_to_node[n] for n in set(self.node_names).difference(nodes_type_a)]
        assert len(nodes_type_a) + len(nodes_type_b) == len(self.nodes)
        return nodes_type_a, nodes_type_b

    def __str__(self) -> str:
        f_str = super().__str__()
        f_str += f"\n- Nodes type a ({len(self.nodes_type_a)}): {self.nodes_type_a}"
        f_str += f"\n- Nodes type b ({len(self.nodes_type_b)}): {self.nodes_type_b}"
        return f_str

    def __repr__(self) -> str:
        return (f"{parsed_str_type(self)} (N:{len(self.nodes)}, A:{len(self.nodes_type_a)} "
                f"B:{len(self.nodes_type_b)}, E:{len(self.edges)}, {repr(self.nodes_state)}")
