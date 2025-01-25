"""
DimNode. Adds dimensionality to the nodes states. Used by EnsembleMP and other mp algorithms requiring heterogeneous
node states.
"""
from typing import Iterable
from .node import Node

class DimNode(Node):
    """
    DimNode implementation
    Parameters:
    - name The name of the node
    - dims The list of integers representing the dimensionality of the node
    """
    def __init__(self, name: str, dims: Iterable[int]):
        assert isinstance(dims, (list, tuple)) and isinstance(dims[0], int), dims
        super().__init__(name)
        self.dims = dims

    def __str__(self) -> str:
        return f"{self.name} {self.dims}"

    def __deepcopy__(self, memo):
        return type(self)(self.name, self.dims)
