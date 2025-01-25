"""Message passing module as a wrapper on top of a Graph object"""
from __future__ import annotations
from abc import abstractmethod, ABC
from collections import namedtuple
from torch import nn
import torch as tr

from ..graph import Graph, NodesState, NodeStatesType
from ..utils import tr_detach_data, to_device, parsed_str_type
from ..logger import nwg_logger as logger

MPMemory = namedtuple("MPMemory", ["messages", "aggregation", "update"])
MessagePassingType = dict[str, list[tr.Tensor]] | tr.Tensor

class MessagePassing(nn.Module, ABC):
    """
    Message passing abstract class. Wraps a graph and defines the `message_pass`, `aggregate`, `update` functions.
    It also defines a standard `forward` method operating on these abstract methods.

    Parameters:
    - graph The graph this MessagePassing layer operates on
    - store_messages If true, the data received at `message_pass`, `aggregate` and `update` are stored in the memory
    of this layer. Upon calling `forward()` again, they are deleted and overwritten. Used for debugging and unit
    testing.
    """
    def __init__(self, graph: Graph, store_messages: bool):
        super().__init__()
        self.graph = graph
        self.store_messages = store_messages
        self.memory = MPMemory(None, None, None)

    # Abstract methods and properties

    @abstractmethod
    def message_pass(self) -> MessagePassingType:
        """Method that defines how messages are sent in one iteration."""

    @abstractmethod
    def aggregate(self, messages: MessagePassingType) -> NodeStatesType:
        """
        Aggregation function that must transform all the received messages of a node to one message after each
        iteration has finished. Basically f(node, [message]) = (node, message).
        """

    @abstractmethod
    def update(self, aggregation: NodeStatesType) -> NodesState:
        """Update function that updates the nodes' representation at the end of each iteration"""

    # Public methods and properties

    def subgraph(self, subgraph: Graph) -> MessagePassing:
        """Implements subgraphing for this message passing module"""
        try:
            return type(self)(subgraph, store_messages=self.store_messages)
        except Exception:
            raise NotImplementedError(f"Subgraphing not implemented for {type(self)}")

    @property
    def device(self) -> tr.device:
        """The device of this message passing module"""
        try:
            return next(self.parameters()).device
        except Exception:
            return tr.device("cpu")

    def is_memory_populated(self) -> bool:
        """Returns true if there is data in the message passing memory. Only true if enabled at ctor time"""
        return self.store_messages and self.memory.messages is not None

    def forward(self, x: NodeStatesType) -> Graph:
        """
        The default forward pass/message passing algorithm:
        - x represents the input data of this message passing, which is the initial state of all given nodes
        - we then do a message passing call, which will send the state of each node to all possible neighbours
        - after the messages are sent, we aggregate them and update the internal state
        - Finally, we return a new graph, with the same edges, but with the updated node states.
        """
        # we clone here because we update its state down below based on the 3 methods in case we use it before fwd().
        self.graph = self.graph.clone()
        self.graph.nodes_state = NodesState(self.graph.node_names, x)
        messages = self.message_pass()
        aggregation = self.aggregate(messages)
        new_states = self.update(aggregation)
        assert isinstance(new_states, NodesState), type(new_states)
        self.graph.nodes_state = new_states

        if self.store_messages:
            logger.debug2(f"Storing messages of {self}")
            self.memory = MPMemory(*to_device(tr_detach_data([messages, aggregation, new_states]), "cpu"))

        return self.graph

    def __str__(self) -> str:
        return f"Layer: '{parsed_str_type(self)}' (memory: {self.is_memory_populated()}) on G: {self.graph}"

    def __repr__(self) -> str:
        return f"Layer '{parsed_str_type(self)}' (memory: {self.is_memory_populated()}) on {repr(self.graph)}"
