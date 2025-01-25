"""EnsembleMP layer"""
from typing import Callable, Any, Mapping
from overrides import overrides
import torch as tr
from torch import nn

from nwgraph.graph import Graph, NodeStatesType, NodesState
from nwgraph.graph.node import DimNode
from nwgraph.pathway import PathwayList as PL, Pathway as P
from nwgraph.message_passing import PathwayListMessagePassing, MessagePassingType

# 1 model per entire mp layer or 1 per edge
ModelOrLazyModel = Callable[[int, int], nn.Module] | nn.Module
EdgeModelType = ModelOrLazyModel | list[ModelOrLazyModel]
EnsembleType = str | Callable[[tr.Tensor], tr.Tensor]

class EnsembleMp(PathwayListMessagePassing):
    """
    EnsembleMP implements a simple ensemble message passing layer. Neightbours are propagated through an learnable
    model and aggregated according to the aggregation function. Update step is done by copying the aggregation.

    Paramters:
    - graph: The graph we do the ensemble message passing to
    - edge_model_type: The callable creating theedge model. Requires 2 params: d_in, d_out. Can be either a Callable or
    a dict of edge names to callables.
    - copy_inputs: Whether the input data (x) is also set as output state at update step
    - all_edges_must_have_data: This adds a check that all edge models receive some input data. Defaults to False.
    See test_ensemble_mp::test_ensemble_mp_fail_edge_wo_input_data
    - ensemble_type: What type of ensembles. Supported: 'mean', 'median' or 'sum' or a lambda function.

    Edge models:
    Each edge receives one model. Now, these models can be provided as simple types or
    as pre-instantiated nn.Modules. If simple types are provided, ten the instantiation is done in this function.
    We use in_dims[0] (same for out_dims) if it has only 1 dimension, otherwise, we use all the dims.
    This allows us to instantiate nn.Linear(in_dims, out_dims) easily. For other type of layers, we need to provide
    a lambda converting node dims to the constructor of the type.

    TODO: think about edge_models being lazily instantiated. Possible weird cases: loading edges and counting params
    """
    def __init__(self, graph: Graph, edge_model_type: EdgeModelType, ensemble_type: EnsembleType,
                 copy_inputs: bool = True, all_edges_must_have_data: bool = False, store_messages: bool = False):
        assert isinstance(edge_model_type, (dict, Callable, nn.Module)), edge_model_type
        assert isinstance(ensemble_type, Callable) or ensemble_type in ("mean", "median", "sum"), ensemble_type
        for node in graph.nodes:
            if not isinstance(node, DimNode):
                raise TypeError(f"Expected dim node, got: {type(graph.nodes[0])}")
        super().__init__(graph, pathways=PL([P([n.name for n in e.nodes]) for e in graph.edges]),
                         store_messages=store_messages)
        self.edge_model_type = edge_model_type
        self.ensemble_type = ensemble_type
        self.copy_inputs = copy_inputs
        self.all_edges_must_have_data = all_edges_must_have_data
        self.aggregation_fn = EnsembleMp.build_aggregation_fn(ensemble_type)
        self._pathway_models: nn.ModuleDict = self._build_models()

    @overrides
    def message_pass(self) -> MessagePassingType:
        """output = {"node1": [msg1, msg2], "node2": [msg3] ... }"""
        res: dict[str, list[tr.Tensor]] = {node: [] for node in self.graph.nodes}
        for edge_name, edge_model in self._pathway_models.items():
            edge = self.graph.name_to_edge[edge_name]
            if not self.graph.nodes_state.is_node_set(edge.input_node):
                if self.all_edges_must_have_data:
                    raise KeyError(f"All edges must have data. Not found for edge '{edge}'")
                continue

            if (edge_input_node_state := self.graph.nodes_state.state.get(edge.input_node)) is None:
                continue

            msg = edge_model(edge_input_node_state)
            res[edge.output_node].append(msg)
        # Only put nodes in the messages dict if any messages were exchanged this step.
        res = {node.name: messages for node, messages in res.items() if len(messages) > 0}
        return res

    @overrides
    def aggregate(self, messages: MessagePassingType) -> NodeStatesType:
        """output = {"node1": f_agg([msg1, msg2]), "node2": f_agg([msg3]) ... }"""
        res = {}
        for node_name, node_messages in messages.items():
            voters = tr.stack(node_messages, dim=0)
            res[node_name] = self.aggregation_fn(voters)
        return res

    @overrides
    def update(self, aggregation: NodeStatesType) -> NodesState:
        """Simplest update step. Return whatever the aggregate function computed."""
        if self.copy_inputs:
            for node_name, state in self.graph.nodes_state.state.items():
                if node_name not in aggregation:
                    aggregation[node_name] = state
        return NodesState(self.graph.node_names, aggregation)

    @staticmethod
    def build_aggregation_fn(ensemble_type: EnsembleType) -> Callable[[tr.Tensor], tr.Tensor]:
        """builds the aggregation fn. staticmethod because it may be used outside of this class as well (ngclib)"""
        if isinstance(ensemble_type, Callable):
            return ensemble_type
        if ensemble_type == "mean":
            return lambda x: x.mean(dim=0)
        if ensemble_type == "median":
            return lambda x: x.median(dim=0).values
        if ensemble_type == "sum":
            return lambda x: x.sum(dim=0)
        raise ValueError(f"Unknown ensemble type: {ensemble_type}")


    @overrides
    def state_dict(self, *args, destination=None, prefix="", keep_vars=False):
        """
        we need to override here because some layers may define other views of the graph at constructor time and
        torch will track these views separately leading to too many items in the dictionary
        """
        return self._pathway_models.state_dict(*args, destination=destination, prefix=prefix, keep_vars=keep_vars)

    @overrides
    def load_state_dict(self, state_dict: Mapping[str, Any], strict: bool=True, assign: bool=False):
        """Calls load_state_dict on the models"""
        return self._pathway_models.load_state_dict(state_dict, strict=strict, assign=assign)

    # Private methods

    def _build_models(self) -> nn.ModuleDict:
        """Gets the edge models. Instantiates them if only types are provided in self.edge_model_type"""
        edge_model_type_dict = self.edge_model_type if isinstance(self.edge_model_type, dict) \
            else {e.name: self.edge_model_type for e in self.graph.edges}

        res = nn.ModuleDict()
        for pathway in self.pathways:
            assert pathway.is_line_pathway() and len(pathway) == 2
            edge = self.graph.nodes_to_edge[tuple(pathway.all_nodes)]
            assert edge.name in edge_model_type_dict, f"Edge {edge.name} not in {edge_model_type_dict}"
            edge_model = edge_model_type_dict[edge.name]
            if not isinstance(edge_model, nn.Module):
                # (5, ) -> just 5. Used as syntactic sugar for for (c_in, c_out) models, such as nn.Linear.
                in_dims = edge.nodes[0].dims[0] if len(edge.nodes[0].dims) == 1 else edge.nodes[0].dims
                out_dims = edge.nodes[-1].dims[0] if len(edge.nodes[-1].dims) == 1 else edge.nodes[-1].dims
                edge_model = edge_model(in_dims, out_dims)
            assert isinstance(edge_model, nn.Module), edge_model
            res[edge.name] = edge_model
        return res
