"""Initialize modules"""
import warnings
import lovely_tensors
from .graph import Graph
from .edge import Edge
from .nodes import Node
from .message_passing import MessagePassing

lovely_tensors.monkey_patch()

warnings.filterwarnings("ignore", "You are using `torch.load` with `weights_only=False`*.")
