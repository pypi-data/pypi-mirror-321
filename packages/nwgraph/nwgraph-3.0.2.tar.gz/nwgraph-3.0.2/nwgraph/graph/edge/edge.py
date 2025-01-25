"""Edge module"""
from __future__ import annotations

from ..node import Node
from ...utils import parsed_str_type, EdgeIndex

class Edge:
    """
    Edge class implementation
    Parameters:
    - nodes: The list of nodes
    - name The name of the edge. If not provided, assigned to "input node -> output node"
    """
    def __init__(self, nodes: list[Node], name: str | None = None):
        assert isinstance(nodes, list)
        for node in nodes:
            assert isinstance(node, Node)
        super().__init__()
        if name is None:
            name = f"{parsed_str_type(self)} ({', '.join([f'{x}' for x in nodes])})"
        self.name = name
        self.nodes = nodes

    @property
    def input_node(self) -> Node:
        """The edge's input node, defaulting to the first one"""
        return self.nodes[0]

    @property
    def output_node(self) -> Node:
        """The edge's output node, defaulting to the last one"""
        return self.nodes[-1]

    @property
    def node_names(self) -> list[str]:
        """The node names as strings"""
        return [node.name for node in self.nodes]

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, x: Edge | str | EdgeIndex | object) -> bool:
        assert isinstance(x, (Edge, str, tuple, list)), type(x)
        if isinstance(x, (tuple, list)):
            return self.nodes == x
        if isinstance(x, Edge):
            return self.name == x.name
        return self.name == x
