"""nodes_state.py module for the class informations and access to the nodes state of a graph"""
import torch as tr

NodeStatesType = dict[str, tr.Tensor] | tr.Tensor

class NodesState:
    """Module for the class providing informations and access to the nodes state of a graph. TODO: abstractize a bit."""
    def __init__(self, node_names: list[str], state: NodeStatesType):
        assert isinstance(state, (dict, tr.Tensor, type(None))), (state, type(state))
        if isinstance(state, tr.Tensor):
            assert len(state) == len(node_names), (node_names, state)
        self.node_names = [*node_names]
        self.state = state

    @property
    def n_nodes_set(self) -> int:
        """The numbers of nodes set according to is_node_set"""
        # (~tr.isnan(nodes_state).reshape((len(self.graph.nodes), -1)).sum(dim=1).type(tr.bool)).sum().item()
        return sum(self.is_node_set(n) for n in self.node_names)

    def is_node_set(self, node_name: str | int) -> bool:
        """returns true if the node is set (state not nan), false otherwise"""
        if self.state is None:
            return False
        if isinstance(self.state, dict):
            return node_name in self.state
        node_ix = self.node_names.index(node_name)
        return not tr.isnan(self.state[node_ix]).any()

    def add_nodes(self, node_names: list[str]):
        """ADds a list of nodes to this nodes state object"""
        assert not any(n in self.node_names for n in node_names), (self.node_names, node_names)
        if isinstance(self.state, dict): # states are spare for the other ones
            self.state = tr.cat([self.state, tr.FloatTensor([tr.nan])])
        self.node_names.extend(node_names)

    def remove_nodes(self, node_names: list[str]):
        """Removes a list of nodes from this nodes state object"""
        assert all(n in self.node_names for n in node_names), (self.node_names, node_names)
        if self.state is None:
            pass
        elif isinstance(self.state, dict):
            for name in node_names:
                if name in self.state:
                    self.state.pop(name)
        else:
            removed_ixs = [self.node_names.index(name) for name in node_names]
            if len(removed_ixs) > 0:
                kept_ix = tr.ones(len(self.state)).bool()
                kept_ix[removed_ixs] = 0
                self.state = self.state[kept_ix]
        self.node_names = [name for name in self.node_names if name not in node_names]

    def __repr__(self):
        if self.state is None:
            return "NS: 0 [None]"
        return f"NS: {self.n_nodes_set} {[*self.state.shape] if isinstance(self.state, tr.Tensor) else '[list]'})"
