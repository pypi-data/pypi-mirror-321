"""Pathway list module"""
from colorama import Fore, Style
from graphviz import Digraph
import numpy as np
from .pathway import Pathway

class PathwayList(list):
    """Pathway list implementation"""
    def __init__(self, pathways: list[Pathway]):
        self.pathways = self._build_pathways(pathways)
        super().__init__(self.pathways)
        self._partial_pathways: list[Pathway] | None = None
        self._dependency_graph: dict[Pathway, list[Pathway]] | None = None
        self._topological_sort: list[Pathway] | None = None
        self._n_steps: int | None = None

    # Properties

    @property
    def partial_pathways(self) -> list[Pathway]:
        """
        Given a list of pathways, merge their partial pathways into a single list. Common paths are put only once.
        Example:
            pathways = [
                P(("a", "b", "c", "d")),
                P(("a", "b", "d", "c", "e")),
                P(("a", "b", "c", "e")),
            ]
            Returns:
            [
                ("a", "b"),
                ("a", "b", "c"), ("a", "b", "d"),
                ("a", "b", "c", "d"), ("a", "b", "c", "e"), ("a", "b", "d", "c"),
                ("a", "b", "d", "c", "e")
            ]
            It should be noted that while [..., "c", "e"] apprears twice, it is not the same pathway, so different edge
            models must be trained and used.
        """
        if self._partial_pathways is not None:
            return self._partial_pathways

        res = set()
        for pathway in self.pathways:
            res.update(pathway.partial_pathways)
        # sort first by length of the path, then by lexicographical order
        self._partial_pathways = sorted(res)
        return self._partial_pathways

    @property
    def all_nodes(self) -> set[str] | set[int]:
        """returns all the nodes in this pathway list by checking each pathway in part"""
        res: set = set()
        for pathway in self.pathways:
            res.update(pathway.all_nodes)
        return res

    @property
    def all_edges(self) -> list[tuple[str, str]]:
        """returns all the edges in this pathway list"""
        res: set = set()
        for pathway in self.pathways:
            res.update(pathway.all_edges)
        return sorted(res)

    @property
    def n_steps(self) -> int:
        """Get the number of steps in the pathway list"""
        if self._n_steps is not None:
            return self._n_steps
        self._n_steps = max(p.n_steps for p in self.pathways)
        return self._n_steps

    @property
    def dependency_graph(self) -> dict[Pathway, list[Pathway]]:
        """Get the dependency graph, used for topo sorting the graph"""
        if self._dependency_graph is not None:
            return self._dependency_graph

        prev_len = 0
        dep_graph = {p: p.partial_pathways for p in self.pathways}
        while prev_len != len(dep_graph):
            new_ones = {}
            prev_len = len(dep_graph)
            for v in dep_graph.values():
                for subpath in v:
                    if subpath not in dep_graph:
                        new_ones[subpath] = subpath.partial_pathways
            dep_graph = dep_graph | new_ones
        self._dependency_graph = dep_graph
        return dep_graph

    # Public methods

    def topological_sort(self) -> list[Pathway]:
        """Compute the topological sort for the list of pathways: pathway -> [subpathways]"""
        if self._topological_sort is not None:
            return self._topological_sort
        # A topological sort can be achieved by sorting by n_steps on the partial pathways. However, there may be
        # partial pathways with the same number of steps, so we add a small number to differentiate.
        steps = np.array([p.n_steps + float(not p.is_line_pathway) / 10 for p in self.partial_pathways])
        sorted_ix = np.argsort(steps)
        self._topological_sort = [self.partial_pathways[i] for i in sorted_ix]
        return self._topological_sort

    def simulate_mp(self) -> list[dict[str | int, list[str | int]]]:
        """Simulates a pathway list. Data is provided at input nodes. ConvergingNodes are aggregations."""
        res: list = [{node_name: [] for node_name in sorted(self.all_nodes)} for _ in range(self.n_steps + 1)]
        # topo_sort (and partial_pathways) also does deduping, so PL([[a, b], [a, c]]) won't have Pathway(a) twice
        topo_sort: list[Pathway] = self.topological_sort()
        timestep_layers = [[p for p in topo_sort if p.n_steps == t] for t in range(self.n_steps + 1)]
        # timestep_layers = [[p for p in topo_sort if p.n_steps + p.delay == t] for t in range(self.n_steps + 1)]

        # TODO-delay-t: We need to implement a delay mechanism here.
        for t in range(self.n_steps + 1):
            for pathway in timestep_layers[t]:
                # P(CP(...)) have no output edges, so its components are already part of the partial_pathways
                if not pathway.has_output_edge() and len(pathway.all_nodes) > 1:
                    continue
                # pathway.nodes_and_paths[t] will throw out of bounds for CPs
                node = pathway.nodes_and_paths[-1]
                res[t][node].append(pathway)
        return res

    def to_graphviz(self) -> Digraph:
        """computes the graphviz representation of the pathway list"""
        g = Digraph(strict=True)
        g.attr(rankdir="LR")
        for pathway in self.pathways:
            g.subgraph(pathway.to_graphviz())
        return g

    # Private methods

    def _build_pathways(self, pathways: list[Pathway]) -> list[Pathway]:
        """converts the list of possible string pathways to Pathway objects"""
        assert all(isinstance(p, Pathway) for p in pathways), f"Pathways must be Pathway objects, got {pathways}"
        # This sorts the list of pathways. We need it because some list of pathways may contains converging pathways
        # plus their components: [a->z, b->z, c->z, CP([[a->z, b->z, c->z], q]])] and we need to guarantee that
        # the CP is the last one. Not sure if this takes care of all the cases.
        return sorted(pathways, key=lambda x: len(x.all_nodes))

    def __str__(self):
        paths = ','.join(str(x) for x in self.pathways)
        return f"PL[{paths}]"

    def __repr__(self):
        paths = f"{Fore.RED},{Style.RESET_ALL}".join(repr(x) for x in self.pathways)
        return f"{Fore.RED}PL[{Style.RESET_ALL}{paths}{Fore.RED}]{Style.RESET_ALL}"
