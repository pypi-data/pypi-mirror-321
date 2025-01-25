"""utils module"""
from typing import Any, T, Iterable
from functools import reduce
import torch as tr
import numpy as np

def prod(x: list[int]) -> int:
    """returns the product of the elements of an integer list"""
    return reduce(lambda a, b: a * b, x, 1)

def parsed_str_type(obj: Any) -> str:
    """returns the stringified type of any object"""
    return str(type(obj)).split(".")[-1][0:-2]

def compare_graph_states(state1: dict[str, tr.Tensor], state2: dict[str, tr.Tensor]) -> dict[str, bool]:
    """
    Returns a dictionary where, for each node we compare the inner torch states. Inputs are {node_name: tr_node_state}.
    Example: state1: {"a": [1], "b": [3]} and {"a": [1], "c": [5]} returns {"a": True, "b": False, "c": False}
    """
    all_keys = sorted(list(set(state1.keys()).union(state2.keys())))
    res = {}
    for key in all_keys:
        # if key is just in one graph's state, then it's not equal
        if key not in state1.keys() or key not in state2.keys():
            res[key] = False
            continue
        res[key] = tr.allclose(state1[key], state2[key])
    return res

def flatten_list(x: Iterable[T]) -> list[T]:
    """Flattens a list of lists. Also flattens np arrays of object type, tuples and sets."""
    if x is None or len(x) == 0:  # type: ignore
        return []
    res = []
    for item in x:
        if isinstance(item, (tuple, list, set)) or (isinstance(item, np.ndarray) and item.dtype == object):
            res.extend(flatten_list(item))
        else:
            res.append(item)
    return res
