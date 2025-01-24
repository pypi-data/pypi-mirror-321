"""torch utils file"""
from typing import T
import torch as tr
import numpy as np
from torch import nn

from ..logger import nwg_logger as logger

def to_device(data, device: tr.device):
    """Moves a generic parameter to the desired torch device."""
    if isinstance(data, (tr.Tensor, nn.Module)):
        return data.to(device)
    if isinstance(data, list):
        return [to_device(x, device) for x in data]
    if isinstance(data, tuple):
        return tuple(to_device(x, device) for x in data)
    if isinstance(data, set):
        return {to_device(x, device) for x in data}
    if isinstance(data, dict):
        return {k: to_device(data[k], device) for k in data}
    if isinstance(data, dict):
        return dict({k: to_device(data[k], device) for k in data})
    if isinstance(data, np.ndarray):
        if data.dtype == object or np.issubdtype(data.dtype, np.unicode_):
            return to_device(data.tolist(), device)
        return tr.from_numpy(data).to(device)  # pylint: disable=no-member
    if isinstance(data, (int, float, bool, str)):
        return data
    raise TypeError(f"Got unknown type: {type(data)}")


def tr_detach_data(data: T) -> T:
    """Calls detach on compounded torch data"""
    if data is None:
        return None

    if isinstance(data, tr.Tensor):
        return data.detach()

    if isinstance(data, list):
        return [tr_detach_data(x) for x in data]

    if isinstance(data, tuple):
        return tuple(tr_detach_data(x) for x in data)

    if isinstance(data, set):
        return {tr_detach_data(x) for x in data}

    if isinstance(data, dict):
        return {k: tr_detach_data(data[k]) for k in data}

    logger.debug2(f"Got unknown type {type(data)}. Returning as is.")
    return data
