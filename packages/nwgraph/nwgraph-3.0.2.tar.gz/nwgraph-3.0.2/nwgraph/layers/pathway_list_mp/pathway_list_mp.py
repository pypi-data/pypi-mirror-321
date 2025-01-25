"""PathwayMp module"""
from typing import Callable
from pathlib import Path
from copy import deepcopy
from overrides import overrides
from torch import nn
import torch as tr

from nwgraph.graph import Graph, NodesState, NodeStatesType
from nwgraph.graph.node import DimNode
from nwgraph.logger import nwg_logger as logger
from nwgraph.message_passing import PathwayListMessagePassing, MessagePassingType
from nwgraph.pathway import ConvergingPathways, PathwayList
from nwgraph.utils import EdgeIndex

from .utils import (MeanEnsemble, SumEnsemble, MedianEnsemble, MpModels,
                    EnsembleFn, AggFnsType, EnsembleType, ModelOrLazyModel)

PathwayListModels = nn.ModuleDict | dict[str, dict[str, nn.Module]]

class PathwayListMp(PathwayListMessagePassing):
    """
    PathwayMp implementation.
    Parameters:
    - graph: The Graph
    - models: All the models of this mp layer. Can be a single model, in which case it will be replicated for all
    pathways.
    - ensemble_type: The type of ensemble to use. We can use a single string/callable, or one per timestep and pathway.
    - pathways: The pathways manually defined as tuples of node names
    """
    def __init__(self, graph: Graph, models: MpModels, ensemble_type: EnsembleType | AggFnsType,
                 pathways: PathwayList, allow_new_nodes_or_edges: bool = False, store_messages: bool = False):
        mp_graph, new_nodes_names, new_edges_indexes = self._get_mp_graph(graph, pathways, allow_new_nodes_or_edges)
        super().__init__(graph=mp_graph, pathways=pathways, store_messages=store_messages)
        self.allow_new_nodes_or_edges = allow_new_nodes_or_edges
        self.model_paths = [x for x in self.pathways.topological_sort()
                            if len(x) > 1 or isinstance(x[0], ConvergingPathways)]
        self.n_models = len(self.model_paths)
        self.model_types = self._build_model_types(models)
        self.ensemble_type = ensemble_type
        self._pathway_list_models = self._build_pathway_list_models()
        self._all_models: nn.ModuleDict | None = None
        self._mp_simulation = self.pathways.simulate_mp()
        self.aggregation_fns: AggFnsType = self._build_aggregation_fns(ensemble_type)
        self.t = -1
        self.latest_state: NodeStatesType = {}

        self.new_nodes_names = new_nodes_names
        self.new_edges_indexes = new_edges_indexes

    @overrides
    def message_pass(self) -> MessagePassingType:
        # we need to pass through all the pathways. Some edges may be shared, so we need to cache their results.
        topo_sort = self.pathways.topological_sort()

        node_states: NodeStatesType = self.graph.nodes_state.state
        assert isinstance(self.graph.nodes_state, NodesState), type(self.graph.nodes_state)
        self.latest_state = node_states

        for t in range(1, self.n_steps + 1):
            node_messages: dict[str, list] = {node.name: [] for node in self.graph.nodes}
            self.t = t
            timestep_layers = [x for x in topo_sort if str(x) in self.all_models and x.n_steps == t]
            for layer in timestep_layers:
                model = self.all_models[str(layer)]
                x_node_name = layer[-2] if isinstance(layer[-2], (str, int)) else layer[-2].converging_node
                y_node_name = layer[-1]
                if x_node_name not in node_states:
                    raise KeyError(f"Node '{x_node_name}' not in {list(node_states.keys())} at t={t}")
                x = node_states[x_node_name]
                y = model(x)
                node_messages[y_node_name].append(y)
            if t != self.n_steps:
                node_states = self.update(self.aggregate(node_messages)).state
            logger.debug(f"Message passing for t={t} finished")
        # return node_messages so forward calls update and aggregate ony more time
        return node_messages

    @overrides
    def aggregate(self, messages: MessagePassingType) -> NodeStatesType:
        """output = {"node1": f_agg([msg1, msg2]), "node2": f_agg([msg3]) ... }"""
        assert isinstance(messages, dict)
        agg = {}
        for node_name, node_messages in messages.items():
            if len(node_messages) > 0:
                votes: tr.Tensor | list = tr.stack(node_messages, dim=0)
                voters = self._mp_simulation[self.t][node_name]
                agg_fn = self.aggregation_fns[str(self.t)][str(node_name)]
                agg[node_name] = agg_fn(votes, voters)
        return agg

    @overrides
    def update(self, aggregation: NodeStatesType) -> NodesState:
        """Simplest update step. Return whatever the aggregate function computed."""
        self.latest_state = self.latest_state | aggregation
        # can this be simplified w/o side effects?
        node_states = aggregation if self.t < self.n_steps else self.latest_state
        return NodesState(self.graph.node_names, node_states)

    @property
    def pathway_list_models(self) -> PathwayListModels:
        """return the pathway models. Keys are the pathway names defined above"""
        return self._pathway_list_models

    @property
    def all_models(self) -> nn.ModuleDict:
        """returns all the models used in this PathwayMp module, indexes by the pathway that this models ends"""
        if self._all_models is not None:
            return self._all_models

        res = nn.ModuleDict()
        for pathway_models in self.pathway_list_models.values():
            for pathway_model_name, pathway_model in pathway_models.items():
                res[pathway_model_name] = pathway_model
        self._all_models = res
        return self._all_models

    def save_all_weights(self, weights_dir: Path):
        """
        Saves the weights of each pathway in a directory. Only the last edge of the path must be stored since
        """
        for model_name, model in self.all_models.items():
            weights_file = Path(f"{weights_dir}/{model_name}/checkpoints/model_best.ckpt")
            weights_file.parent.mkdir(exist_ok=True, parents=True)
            tr.save({"state_dict": model.state_dict()}, weights_file)
        tr.save({"state_dict": self.aggregation_fns.state_dict()}, f"{weights_dir}/agg_fns.ckpt")

    def load_all_weights(self, weights_dir: Path):
        """Loads all weights from a directory"""
        for model_name, model in self.all_models.items():
            weights_file = Path(f"{weights_dir}/{model_name}/checkpoints/model_best.ckpt")
            weights_file.parent.mkdir(exist_ok=True, parents=True)
            assert weights_file.exists(), weights_file
            logger.debug(f"Loading weights for '{model_name}' from '{weights_file}'")
            data = tr.load(weights_file, map_location="cpu")["state_dict"]
            model.load_state_dict(data)
        self.aggregation_fns.load_state_dict(tr.load(f"{weights_dir}/agg_fns.ckpt", map_location="cpu")["state_dict"])
        logger.info(f"Successfully loaded weights for {self}.")

    # Private methods

    # pylint: disable=unused-argument
    def _get_mp_graph(self, graph: Graph, pathways: PathwayList, allow_new_nodes_or_edges: bool) \
            -> tuple[Graph, list[str], list[EdgeIndex]]:
        # PathwayListMp works with DimNodes only
        for node in graph.nodes:
            assert isinstance(node, DimNode), f"Node {node} is not a DimNode, but {type(node)}"
        new_nodes_names = set(pathways.all_nodes).difference(graph.node_names)
        new_edges_indexes = set(pathways.all_edges).difference(graph.edge_indexes)
        assert (len(new_nodes_names) == 0 and len(new_edges_indexes) == 0) or allow_new_nodes_or_edges, \
            f"New nodes or edges found: {new_nodes_names}, {new_edges_indexes}. Set allow_new_nodes_or_edges=True."

        if len(new_nodes_names) == 0 and len(new_edges_indexes) == 0:
            return graph, [], []

        for node in graph.nodes:
            assert "_" not in node.name, f"Node name '{node.name}' contains '_'. Not allowed when adding new nodes."

        # We assume that the new nodes contain '_' once which concatenates the two original nodes.
        # This must be a CatNode. Nothing else is allowed here.
        new_nodes_args = []
        for node in new_nodes_names:
            orig_nodes = node.split("_")
            assert len(orig_nodes) == 2, f"Node name '{node}' doesn't contain exactly one '_'."
            node_a, node_b = graph.name_to_node[orig_nodes[0]], graph.name_to_node[orig_nodes[1]]
            # dims must match exactly, except last dim of both nodes. New dim concatenates the two on the last axis.
            assert node_a.dims[0:-1] == node_b.dims[0:-1], (node_a.dims, node_b.dims)
            new_dims = (*node_a.dims[0:-1], node_a.dims[-1] + node_b.dims[-1])
            new_nodes_args.append({"dims": new_dims})

        new_graph = deepcopy(graph)
        new_nodes_types = [DimNode for _ in range(len(new_nodes_names))]
        new_graph.add_nodes(new_nodes_names, new_nodes_types, new_nodes_args)
        new_graph.add_edges(new_edges_indexes)
        return new_graph, new_nodes_names, new_edges_indexes

    def _build_model_types(self, mp_models: MpModels) -> list[ModelOrLazyModel]:
        assert isinstance(mp_models, (type, Callable, list)), mp_models
        mp_models_list: list
        # We have 1 model for each entry in the topological sort of all pathways. Some paths may be shared, so this
        # is we require to make a topo sort. Some paths may be different even though we have the same local edge
        # (node_in, node_out), but their pathway history is different.
        # we also ignore P(a) here, so one node is not enough for a model, these are input nodes.
        if isinstance(mp_models, (type, Callable)):
            mp_models_list = [mp_models for _ in range(self.n_models)]
        else:
            assert isinstance(mp_models, list)
            mp_models_list = mp_models
        if len(mp_models_list) != self.n_models:
            raise ValueError(f"Expected {self.n_models} models, got {len(mp_models_list)}")
        return mp_models_list

    def _build_pathway_list_models(self) -> PathwayListModels:
        """
        Gets the pathway models. Instantiates them if only types are provided in self.edge_model_type
        Note: we use str(pathway) because pytorch doesn't allow nn.ModuleDict to have non-strings as keys.
        """

        # step 1: we build the pathway models based on the dependency graph. This ensures that we build the model only
        # once even if it is used in multiple pathways.
        models = {}
        topo_sort_models = [x for x in self.pathways.topological_sort() if len(x) > 1]
        for pathway, deps in self.pathways.dependency_graph.items():
            for dep in deps:
                # len(dep) == 1 catches both P(a) and P(CP{(a,X),(b,X)})
                if len(dep) == 1 or dep in models:
                    continue
                model_ix = topo_sort_models.index(dep)
                model = self.model_types[model_ix]
                if not isinstance(model, nn.Module):
                    out_node = self.graph.name_to_node[dep[-1]]
                    in_node_name = dep[-2] if isinstance(dep[-2], (str, int)) else dep[-2].converging_node
                    in_node = self.graph.name_to_node[in_node_name]
                    assert isinstance(in_node, DimNode) and isinstance(out_node, DimNode), (in_node, out_node)
                    # Syntactic sugar for (c_in, c_out) models, such as nn.Linear. Transforms tuple (5, ) to 5.
                    in_dims = in_node.dims[0] if len(in_node.dims) == 1 else in_node.dims
                    out_dims = out_node.dims[0] if len(out_node.dims) == 1 else out_node.dims
                    # This is mostly for debugging purposes
                    try:
                        model = model(in_dims, out_dims)
                    except TypeError as e:
                        logger.debug(f"Torch module init failed. Model: {model}. Params: in={in_dims}, out={out_dims}")
                        raise TypeError(e)
                models[dep] = model

        # step 2: use these instantiated models to build the pathway models. Using strings as keys due to torch.
        res = nn.ModuleDict()
        for pathway in self.pathways:
            pathway_res = nn.ModuleDict()
            for subpath in pathway.partial_pathways:
                if len(subpath) == 1:
                    continue
                pathway_res[str(subpath)] = models[subpath]
            res[str(pathway)] = pathway_res

        logger.info(f"Built {len(res)} path models for {repr(self)}.")
        return res

    def _build_one_agg_fn(self, ensemble_type: str | EnsembleFn) -> EnsembleFn:
        """string or callable as input, returns a callable"""
        assert isinstance(ensemble_type, (str, Callable)), ensemble_type
        if isinstance(ensemble_type, str):
            if ensemble_type == "mean":
                return MeanEnsemble()
            if ensemble_type == "median":
                return MedianEnsemble()
            if ensemble_type == "sum":
                return SumEnsemble()
        else:
            return ensemble_type
        raise ValueError(f"Unknown ensemble type: {ensemble_type}")

    def _build_aggregation_fns(self, ensemble_type: EnsembleType) -> AggFnsType:
        """we build one aggregation type for each timestep and for each node."""
        res = nn.ModuleDict()

        if isinstance(ensemble_type, str):
            # lift from 'str' to the list of dicts only for valid pathways
            for t in range(1, self.n_steps + 1):
                res[str(t)] = nn.ModuleDict()
                for node in self.graph.nodes:
                    if node.name not in self._mp_simulation[t]:
                        raise KeyError(f"Node {node.name} not found at t={t}. Nodes: {list(self._mp_simulation[t])}")
                    if len(self._mp_simulation[t][node.name]) > 0:
                        res[str(t)][str(node.name)] = self._build_one_agg_fn(ensemble_type)
            return res

        if isinstance(ensemble_type, dict):
            # lift from dicts w/o timestamps
            for t in range(1, self.n_steps + 1):
                res[str(t)] = nn.ModuleDict()
                for node in self.graph.nodes:
                    if node.name not in self._mp_simulation[t]:
                        raise KeyError(f"Node {node.name} not found at t={t}. Nodes: {list(self._mp_simulation[t])}")
                    if len(self._mp_simulation[t][node.name]) > 0:
                        res[str(t)][str(node.name)] = self._build_one_agg_fn(ensemble_type[node.name])
            return res

        assert isinstance(ensemble_type, list), ensemble_type
        assert len(ensemble_type) == self.n_steps, f"{len(ensemble_type)} != {self.n_steps}"

        for t in range(1, self.n_steps + 1):
            res[str(t)] = nn.ModuleDict()
            t_ensemble = ensemble_type[t - 1]

            if isinstance(t_ensemble, str):
                # lift from 'str' at this timestemp to valid timestep pathways only
                for node in self.graph.nodes:
                    if node.name not in self._mp_simulation[t]:
                        raise KeyError(f"Node {node.name} not found at t={t}. Nodes: {list(self._mp_simulation[t])}")
                    if len(self._mp_simulation[t][node.name]) > 0:
                        res[str(t)][str(node.name)] = self._build_one_agg_fn(t_ensemble)
                continue

            assert isinstance(t_ensemble, dict), t_ensemble

            for node in self.graph.nodes:
                # error if we provide explicit nodes and timestamps but wrong.
                if node.name not in self._mp_simulation[t]:
                    raise KeyError(f"Node {node.name} not found at t={t}. Nodes: {list(self._mp_simulation[t])}")
                if len(self._mp_simulation[t][node.name]) == 0:
                    if node.name in t_ensemble:
                        raise ValueError(f"Node '{node.name}' shouldn't have an agg fn for t={t}: {t_ensemble}")
                    continue
                if node.name not in t_ensemble:
                    raise KeyError(f"Node '{node.name}' doesn't have an agg fn for t={t}: {t_ensemble}")

                res[str(t)][str(node.name)] = self._build_one_agg_fn(t_ensemble[node.name])
        return res
