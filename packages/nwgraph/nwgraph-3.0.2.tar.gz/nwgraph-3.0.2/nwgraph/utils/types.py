"""Fundamental types for nwgraph"""
from typing import Type, List, Tuple, Dict, Any

# [ [1, 2], [3, 4]] or [ [a, b], [c, d] ]. For 2nd we need node_names too.
EdgeIndex = Tuple[str, str]
# {"arg1": "param1"...} or [{"arg1": "param1", ...}, ... (other nodes args) ...]
NodeArgs = Dict[str, Any] | List[Dict[str, Any]]
# Type or [Type, ..., Type], 1 for each node
NodeTypes = Type["Node"] | List[Type["Node"]]  # noqa: F821
# Type or [Type, ..., Type], 1 for each edge
EdgeTypes = Type["Edge"] | List[Type["Edge"]]  # noqa: F821
