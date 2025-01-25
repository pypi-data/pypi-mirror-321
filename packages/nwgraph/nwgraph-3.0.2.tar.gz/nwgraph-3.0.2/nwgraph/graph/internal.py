"""internal module to build the graph so we don't pollute the main class file"""
# pylint: disable=protected-access
from copy import copy, deepcopy
from typing import Type
from functools import reduce

from ..utils import EdgeIndex, NodeArgs
from ..logger import nwg_logger as logger
from .node import Node

def graph_subgraph(self: "Graph", edge_names_or_indexes: list[str] | list[EdgeIndex], prune_nodes: bool) -> "Graph":
    """computes the subgraph given edge names or indexes"""
    # TODO: Perhaps sort edge_indexes at ctor time and binary search
    # TODO: shrink unused nodes? or just pruned nodes from previous graph
    assert isinstance(edge_names_or_indexes[0], (str, list, tuple)), \
        "edge_names_or_indexes must be a list of edge names or a list of edge indexes"

    if isinstance(edge_names_or_indexes[0], str):
        new_indexes_ixs = [self.edges.index(e_name) for e_name in edge_names_or_indexes]
    else:
        # EdgeIndex can be list[tuple[str, str]] or list[tuple[int, int]]
        edge_names_or_indexes = build_edge_indexes(self, edge_names_or_indexes)
        new_indexes_ixs = [self.edge_indexes.index(e_ix) for e_ix in edge_names_or_indexes]

    self_copy = copy(self)
    self_copy.edge_indexes = [self_copy.edge_indexes[ix] for ix in new_indexes_ixs]
    self_copy.n_edges = len(self_copy.edge_indexes)
    self_copy.edge_types = [self_copy.edge_types[ix] for ix in new_indexes_ixs]
    self_copy._edges = [self_copy.edges[ix] for ix in new_indexes_ixs]
    self_copy._adjacency_matrix = None
    self_copy._name_to_edge = None

    if prune_nodes:
        new_node_names = set()
        for edge in self_copy.edges:
            new_node_names.update(edge.nodes)
        node_ixs = [self.nodes.index(node) for node in new_node_names]

        self_copy.n_nodes = len(node_ixs)
        self_copy.node_names = [self.node_names[ix] for ix in node_ixs]
        self_copy.node_types = [self.node_types[ix] for ix in node_ixs]
        self_copy.node_args = [self.node_args[ix] for ix in node_ixs]
        self_copy._nodes = None
        self_copy._name_to_node = None

        self_copy.nodes_state = deepcopy(self.nodes_state)
        self_copy.nodes_state.remove_nodes([n for n in self.nodes if n not in new_node_names])

    return self_copy

def build_node_names(node_names: list[str] | None, edge_indexes: list[EdgeIndex]) -> list[str]:
    """builds the node names"""
    if node_names is None:
        unique_nodes = sorted(reduce(lambda a, b: a.union(b), edge_indexes, set()))
        nodes_str = unique_nodes if len(unique_nodes) < 10 else f"uniques from edge_indexes ({len(unique_nodes)} nodes)"
        logger.debug(f"Node names not provided. Defaulting to {nodes_str}")
        node_names = unique_nodes
    assert all(isinstance(node_name, str) for node_name in node_names), "Not all node names are strings/ints"
    return node_names

def build_node_types(n_nodes: int, node_types: Type | list[Type] | None) -> list[Type]:
    """builds the nodes types. If not provided, it defaults to list of Node types"""
    assert isinstance(node_types, (Type, list, type(None))), f"{node_types} is not a Type or a list of Types"
    node_types = Node if node_types is None else node_types
    node_types = [node_types for _ in range(n_nodes)] if not isinstance(node_types, list) else node_types
    assert len(node_types) == n_nodes, f"{len(node_types)} vs {n_nodes}"
    return node_types

def get_n_nodes(edge_indexes: list[EdgeIndex], n_nodes: int | None, node_names: list[str] | None) -> int:
    """gets the number of nodes from the edge_indexes or n_nodes"""
    assert isinstance(n_nodes, (int, type(None))), type(n_nodes)

    if n_nodes is not None:
        return n_nodes

    if node_names is not None:
        return len(node_names)

    unique_nodes = reduce(lambda a, b: a.union(b), edge_indexes, set())
    logger.debug(f"Node names not provided. n_nodes is set to {len(unique_nodes)}")
    return len(unique_nodes)

def build_node_args(n_nodes: int, node_args: NodeArgs | None) -> NodeArgs:
    """build the node args. If None, will create an empty array"""
    node_args = node_args if node_args is not None else [{} for _ in range(n_nodes)]
    assert isinstance(node_args, (list, dict)), type(node_args)
    node_args = node_args if isinstance(node_args, list) else [node_args for _ in range(n_nodes)]
    assert isinstance(node_args, list) and isinstance(node_args[0], dict), type(node_args)
    return node_args

def check_graph(self: "Graph"):
    """checks that the graph was created properly (same n_edges and same n_nodes as names/types/args etc.)"""
    n_nodes = len(self.nodes)
    assert len(self.node_names) == n_nodes, f"{len(self.node_names)} vs {n_nodes}"
    assert len(self.node_types) == n_nodes, f"{len(self.node_types)} vs {n_nodes}"
    assert len(self.node_args) == n_nodes, f"{len(self.node_args)} vs {n_nodes}"

    n_edges = len(self.edges)
    assert len(self.edge_types) == n_edges, f"{len(self.edge_types)} vs {n_edges}"
    assert len(self.edge_indexes) == n_edges, f"{len(self.edge_indexes)} vs {n_edges}"

def build_edge_indexes(self: "Graph", edge_indexes: list) -> list[EdgeIndex]:
    """builds the edge_indexes"""
    res = []
    uniqs = set()
    for edge_index in edge_indexes:
        assert all(lambda x: isinstance(x, str) for x in edge_index), f"{edge_index} is not a list of strings"
        uniqs.update(edge_index)
        res.append(tuple(edge_index))
    assert uniqs.intersection(self.node_names) == uniqs, f"unknown node names: {uniqs - set(self.node_names)}"
    return res
