"""Node module"""
from __future__ import annotations
from ...utils import parsed_str_type

class Node:
    """NWgraph Node class with a name"""
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"{parsed_str_type(self)}({self.name})"

    def __repr__(self) -> str:
        return str(self)

    # This and __eq__ are used so we can put node in dict and access them via strings
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, x: Node | str) -> bool:
        other_name = x.name if isinstance(x, Node) else x
        return self.name == other_name

    def __lt__(self, x: Node | str) -> bool:
        other_name = x.name if isinstance(x, Node) else x
        return self.name < other_name

    def __ge__(self, x: Node | str) -> bool:
        other_name = x.name if isinstance(x, Node) else x
        return self.name >= other_name

    def __deepcopy__(self, memo):
        return type(self)(self.name)
