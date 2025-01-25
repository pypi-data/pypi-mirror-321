"""Graph abstract class module"""
from __future__ import annotations
from copy import deepcopy, copy
from typing import Dict, Type, overload
from functools import partial
from graphviz import Digraph
import networkx as nx
import torch as tr

from ..utils import parsed_str_type, EdgeIndex, NodeArgs, EdgeTypes, NodeTypes
from .node import Node
from .edge import Edge
from .internal import (graph_subgraph, get_n_nodes, build_node_names, build_node_types,
                       build_node_args, check_graph, build_edge_indexes)
from .nodes_state import NodesState

class Graph:
    """
    Graph class. The main object of this library. Holds the nodes and the edge indexes.
    TODO: edge args -- perhaps this is part of MP class.

    Parameters:
    - edge_indexes: The list of nodes pairs used for edges. Can be indexes or strings. If strings, we must also provide
    the node names.
    - n_nodes: The number of nodes. If not provided, it's infered from edge_indexes.
    - edge_types: The type of edges. Used to instantiate the edges. If not provided, defaults to `nwgraph.Edge`.
    - node_names: The node names. If not provided, it'll default to integer names based on edge_indexes. Must be
    provided if edge_indexes is based on node names (strings).
    - node_types: The type of nodes. Used to instantiate the nodes. If not provided, defaults to `nwgraph.Node`.
    - node_args: The arguments of each node. If `node_types` has a different constructor than `nwgraph.Node(name: str)`
    , this dictionary must be provided.
    """
    def __init__(self, edge_indexes: list[EdgeIndex], n_nodes: int | None = None,
                 edge_types: EdgeTypes | None = None, node_names: list[str] | None = None,
                 node_types: NodeTypes | None = None, node_args: NodeArgs | None = None):
        assert isinstance(edge_indexes, list), type(edge_indexes)
        assert len(edge_indexes) == 0 or isinstance(edge_indexes[0], (tuple, list)), type(edge_indexes[0])

        _n_nodes = get_n_nodes(edge_indexes, n_nodes, node_names)
        self.node_names: list = build_node_names(node_names, edge_indexes)
        self.node_types: list[Type[Node]] = build_node_types(_n_nodes, node_types)
        self.node_args = build_node_args(_n_nodes, node_args)
        self._nodes: list[Node] | None = None
        self._name_to_node: Dict[str, Node] | None = None
        self._nodes_state = NodesState(node_names=self.node_names, state=None)

        self.edge_indexes = build_edge_indexes(self, edge_indexes)
        self.edge_types: list[Type[Edge]] = [Edge for _ in range(len(self.edge_indexes))] \
            if edge_types is None else edge_types
        self._edges: list[Edge] | None = None
        self._name_to_edge: Dict[str, Edge] | None = None
        self._adjacency_matrix: tr.Tensor | None = None
        self._nodes_to_edge: dict[tuple[str, ...], Edge] | None = None

        check_graph(self)

    # Public properties

    @property
    def name_to_node(self) -> Dict[str, Node]:
        """A dictionary between node names and the nodes. Lesson: always cache as this is O(n)."""
        if self._name_to_node is None:
            self._name_to_node = {node.name: node for node in self.nodes}
        return self._name_to_node

    @property
    def name_to_edge(self) -> Dict[str, Edge]:
        """A dictionary between edge names and the edges"""
        if self._name_to_edge is None:
            self._name_to_edge = {edge.name: edge for edge in self.edges}
        return self._name_to_edge

    @property
    def nodes_to_edge(self) -> dict[tuple[str, ...], Edge]:
        """A dictionary between a tuple of node names and the corresponding edge"""
        if self._nodes_to_edge is None:
            self._nodes_to_edge = {tuple(n.name for n in edge.nodes): edge for edge in self.edges}
        return self._nodes_to_edge

    @property
    def nodes(self) -> list[Node]:
        """The nodes of the graph"""
        if self._nodes is None:
            self._nodes = [node_type(node_name, **node_args) for node_type, node_name, node_args
                           in zip(self.node_types, self.node_names, self.node_args)]
        return self._nodes

    @property
    def edges(self) -> list[Edge]:
        """The edges of the graph"""
        if self._edges is None:
            self._edges = [edge_type([self.name_to_node[ix] for ix in e_ix])
                           for edge_type, e_ix in zip(self.edge_types, self.edge_indexes)]
        return self._edges

    @property
    def adjacency_matrix(self) -> tr.Tensor:
        """Returns the adjacency matrix"""
        if self._adjacency_matrix is None:
            A = tr.zeros(len(self.nodes), len(self.nodes)).type(tr.LongTensor)
            edge_indexes = [[self.node_names.index(a), self.node_names.index(b)] for a, b in self.edge_indexes]
            where = tr.IntTensor(edge_indexes)
            A[where[:, 0], where[:, 1]] = 1
            self._adjacency_matrix = A #.to_sparse()
        return self._adjacency_matrix

    @property
    def n_nodes_set(self) -> int:
        """The number of nodes not in an empty state"""
        return self.nodes_state.n_nodes_set

    @property
    def nodes_state(self) -> NodesState:
        """returns the nodes state"""
        return self._nodes_state

    @nodes_state.setter
    def nodes_state(self, nodes_state: NodesState):
        assert isinstance(nodes_state, NodesState), type(nodes_state)
        self._nodes_state = nodes_state

    # Public methods

    def get_neighbours(self, node_name: str | int) -> tuple[list, list]:
        """returns the neighbours of a node"""
        if node_name not in self.node_names:
            raise KeyError(f"Node {node_name} doesn't exist in the graph.")
        node_ix = self.node_names.index(node_name)
        incoming = sorted(self.node_names[ix] for ix in tr.where(self.adjacency_matrix[:, node_ix] != 0)[0])
        outgoing = sorted(self.node_names[ix] for ix in tr.where(self.adjacency_matrix[node_ix] != 0)[0])
        return incoming, outgoing

    def add_nodes(self, node_names: list[str] | list[int], node_types: list[Type[Node]], node_args: list[NodeArgs]):
        """adds new nodes to the graph. If they already exists, it'll throw an exception"""
        assert len(node_names) == len(node_types) == len(node_args), (len(node_names), len(node_types), len(node_args))
        for node_name, node_type, node_arg in zip(node_names, node_types, node_args):
            assert node_name not in self.name_to_node, f"Node {node_name} already exists in the graph."
            node = node_type(name=node_name, **node_arg)
            self._nodes.append(node)
            self.node_names.append(node_name)
            self.node_types.append(node_type)
            self.node_args.append(node_arg)
            self._adjacency_matrix = None
            self._name_to_node = None
        self.nodes_state.add_nodes(node_names)

    def remove_nodes(self, node_names: list[str] | list[int]):
        """removes nodes from the graph using their names. If they don't exist, it'll throw an exception"""
        edges_to_remove = []
        for node_name in node_names:
            neigh_in, neigh_out = self.get_neighbours(node_name)
            for neigh in neigh_in:
                edges_to_remove.append((neigh, node_name))
            for neigh in neigh_out:
                edges_to_remove.append((node_name, neigh))

            node_ix = self.node_names.index(node_name)
            self._nodes.pop(node_ix)
            self.node_names.pop(node_ix)
            self.node_types.pop(node_ix)
            self.node_args.pop(node_ix)
            self.remove_edges(edges_to_remove)
            self._name_to_node = None
        self.nodes_state.remove_nodes(node_names)

    def add_edges(self, edge_indexes: list[EdgeIndex], edge_types: EdgeTypes | None = None):
        """adds new edges to the graph. Nodes must exist in the graph already."""
        edge_types = edge_types if edge_types is not None else [Edge for _ in range(len(edge_indexes))]
        assert len(edge_indexes) == len(edge_types), (len(edge_indexes), len(edge_types))
        for edge_index, edge_type in zip(edge_indexes, edge_types):
            assert edge_index not in self.edge_indexes, f"Edge {edge_index} already exists in the graph."
            assert edge_index[0] in self.node_names, f"Node {edge_index[0]} not in the graph: {self.node_names}"
            assert edge_index[1] in self.node_names, f"Node {edge_index[1]} not in the graph: {self.node_names}"

        for edge_index, edge_type in zip(edge_indexes, edge_types):
            edge = edge_type([self.name_to_node[ix] for ix in edge_index])
            self._edges.append(edge)
            self.edge_indexes.append(tuple(edge_index))
            self.edge_types.append(edge_type)

            self._name_to_edge = None
            self._nodes_to_edge = None
            self._adjacency_matrix = None

    def remove_edges(self, edge_indexes: list[EdgeIndex]):
        """removes edges"""
        for edge_index in edge_indexes:
            assert edge_index in self.edge_indexes, f"Edge {edge_index} doesn't exist in the graph: {self.edge_indexes}"
            edge_ix = self.edge_indexes.index(edge_index)
            self._edges.pop(edge_ix)
            self.edge_indexes.pop(edge_ix)
            self.edge_types.pop(edge_ix)

            self._name_to_edge = None
            self._nodes_to_edge = None
            self._adjacency_matrix = None

    def readout(self) -> tr.Tensor | Dict[str, list[tr.Tensor]] | None:
        """the state of all nodes in the graph"""
        return self.nodes_state.state

    def print_nodes_state(self):
        """Prints all the nodes states"""
        for node in self.nodes:
            print(repr(node))

    @overload
    def subgraph(self, edge_names_or_indexes: list[str], prune_nodes: bool) -> Graph:
        """subgraph by a list of edge indexes or a list of edge names"""

    @overload
    def subgraph(self, edge_names_or_indexes: list[EdgeIndex], prune_nodes: bool) -> Graph:
        """subgraph by a list of edge indexes"""

    # pylint: disable=protected-access
    def subgraph(self, edge_names_or_indexes: list[str] | list[EdgeIndex], prune_nodes: bool = False) -> Graph:
        """
        Subgraph method. It supports both a list of edge names (strings) or a list of edge indexes
        Parameters:
        - edge_names_or_indexes: a list of edge names or a list of edge indexes
        - prune_nodes: if True, nodes that are not connected to any edge will be pruned
        """
        return graph_subgraph(self, edge_names_or_indexes, prune_nodes)

    def clone(self) -> Graph:
        """clones this particular graph"""
        return type(self)(edge_indexes=deepcopy(self.edge_indexes),
                          n_nodes=len(self.nodes),
                          edge_types=copy(self.edge_types),
                          node_names=copy(self.node_names),
                          node_types=copy(self.node_types),
                          node_args=deepcopy(self.node_args))

    # Visualisation methods

    def to_graphviz(self, **kwargs) -> Digraph:
        """Returns a graphviz object from this graph. Used for plotting the graph. Best for smaller graphs."""
        g = Digraph()
        for k, v in kwargs.items():
            g.attr(**{k: v})
        g.attr(rankdir="LR")
        for node in self.nodes:
            color = "blue" if self.nodes_state.is_node_set(node.name) else "black"
            g.node(name=f"{node.name}", shape="oval", color=color)
        for i in range(len(self.edges)):
            edge = self.edges[i]
            g.edge(f"{edge.input_node.name}", f"{edge.output_node.name}", label=edge.name)
        return g

    def to_networkx(self, **kwargs) -> nx.Graph:
        """Returns a networkx object from this graph. Used for plotting the graph. Best for larger graphs."""
        G = nx.Graph()
        G.add_nodes_from(range(len(self.nodes)))
        G.add_edges_from(self.edge_indexes)
        setattr(G, "draw", partial(nx.draw, G=G, **kwargs))
        return G

    # Private methods

    def __str__(self) -> str:
        f_str = "Graph:"
        f_str += f"\n- Type: {parsed_str_type(self)}"
        if len(self.nodes) < 20:
            f_str += f"\n- Nodes ({len(self.nodes)}): [{', '.join([str(n) for n in self.nodes])}]"
        else:
            f_str += f"\n- Nodes: {len(self.nodes)}"
        if len(self.edges) < 10:
            edges_str = []
            for edge in self.edges:
                edges_str.append(f"{parsed_str_type(edge)}(" + "->".join([str(_n) for _n in edge.nodes]) + ")")
            f_str += f"\n- Edges ({len(self.edges)}): {', '.join(edges_str)}"
        else:
            f_str += f"\n- Edges: {len(self.edges)}"
        f_str += f"\n- States set: {self.n_nodes_set}"
        return f_str

    def __repr__(self) -> str:
        return f"{parsed_str_type(self)} (N:{len(self.nodes)}, E:{len(self.edges)}, {repr(self.nodes_state)}"

    def __eq__(self, other: Graph) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self.node_names != other.node_names:
            return False

        if self.node_types != other.node_types:
            return False

        if self.node_args != other.node_args:
            return False

        if self.edge_indexes != other.edge_indexes:
            return False

        if self.edge_types != other.edge_types:
            return False

        return True
