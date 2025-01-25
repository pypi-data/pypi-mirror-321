"""PathwayBuilder -- build Pathways, ConvergingPathways or PathwayList objects from simple strings or partial strings"""
from .pathway import Pathway as P
from .converging_pathways import ConvergingPathways as CP
from .pathway_list import PathwayList as PL

def pathway_builder(pathway_data: list[str] | list[int], add_delay_to_cp: bool = True):
    """pathway_builder implementation"""
    assert isinstance(pathway_data, (list, tuple)), pathway_data
    assert all(isinstance(x, (str, int, list, tuple, P, CP, PL)) for x in pathway_data), pathway_data

    # We try to convert all the inner lists recursively from the get go
    res = []
    for item in pathway_data:
        res.append(pathway_builder(item) if isinstance(item, (list, tuple)) else item)

    # If all are ints or strings, construct a pathway
    if all(isinstance(x, (str, int, CP)) for x in res):
        return P(res)

    # Otherwise, we have a list of lists here (P or CP). If all the last elements are the same, we have a CP.
    cp_cond = all(x[-1] == res[0][-1] for x in res)
    if cp_cond:
        return CP(res, add_delays=add_delay_to_cp)

    # Otherwise, we have a plain list of pathways
    return PL(res)
