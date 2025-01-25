"""torch utils file"""
from typing import T
import torch as tr
import numpy as np
from torch import nn

from ..logger import nwg_logger as logger

def to_device(data, device: tr.device):
    """Moves a generic parameter to the desired torch device."""
    if data is None:
        return None
    if isinstance(data, (tr.Tensor, nn.Module)) or hasattr(data, "to"):
        return data.to(device)
    if isinstance(data, list):
        return type(data)([to_device(x, device) for x in data])
    if isinstance(data, tuple):
        if hasattr(data, "_asdict"): # NameTuple
            return type(data)(**to_device(data._asdict(), device)) # pylint: disable=protected-access
        return type(data)(to_device(x, device) for x in data)
    if isinstance(data, set):
        return type(data)({to_device(x, device) for x in data})
    if isinstance(data, dict):
        return type(data)({k: to_device(data[k], device) for k in data})
    if isinstance(data, np.ndarray):
        if data.dtype == object:
            return to_device(data.tolist(), device)
        return tr.from_numpy(data).to(device)  # pylint: disable=no-member
    if isinstance(data, (int, float, bool, str)):
        return data
    logger.debug2(f"Got unknown type {type(data)}. Returning as is.")
    return data

def tr_detach_data(data: T) -> T:
    """Calls detach on compounded torch data"""
    if data is None:
        return None
    if isinstance(data, tr.Tensor) or hasattr(data, "detach"):
        return data.detach()
    if isinstance(data, list):
        return type(data)([tr_detach_data(x) for x in data])
    if isinstance(data, tuple):
        if hasattr(data, "_asdict"): # NameTuple
            return type(data)(**tr_detach_data(data._asdict())) # pylint: disable=protected-access
        return type(data)(tr_detach_data(x) for x in data)
    if isinstance(data, set):
        return type(data)({tr_detach_data(x) for x in data})
    if isinstance(data, dict):
        return type(data)({k: tr_detach_data(data[k]) for k in data})

    logger.debug2(f"Got unknown type {type(data)}. Returning as is.")
    return data
