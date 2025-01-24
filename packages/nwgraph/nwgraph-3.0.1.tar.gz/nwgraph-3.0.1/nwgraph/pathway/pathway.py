"""pathways module -- handles the creation of pathways and path models"""
# pylint: disable=import-outside-toplevel, cyclic-import
from __future__ import annotations
from colorama import Fore, Style
from graphviz import Digraph

from ..graph import Graph
from ..logger import nwg_logger as logger

class Pathway:
    """Pathway class"""
    # TODO-delay-t: We need to implement a delay mechanism here. This is needed for ConvergingPathways that may
    #  start a bit later. See also simulate_mp in pathway_list.
    def __init__(self, nodes_and_paths: list["ConvergingPathways" | str | int], delay: int = 0):
        if isinstance(nodes_and_paths, str):
            logger.warning("This will be removed at some point, so we should fix.")
        self.nodes_and_paths: tuple = self._build_nodes_and_paths(nodes_and_paths)
        self._partial_pathways: list[Pathway] | None = None
        self._n_steps: int | None = None
        self._check_pathway()
        self.delay = delay

    # Properties

    @property
    def partial_pathways(self) -> list[Pathway]:
        """returns all the partial pathways given this pathway"""
        if self._partial_pathways is not None:
            return self._partial_pathways
        self._partial_pathways = self._build_partial_pathways()
        return self._partial_pathways

    @property
    def n_steps(self) -> int:
        """returns the number of steps from the first input node, to the first output node"""
        if self._n_steps is not None:
            return self._n_steps
        res = self.delay
        for node_or_path in self.nodes_and_paths:
            res += 1 if isinstance(node_or_path, (str, int)) else node_or_path.n_steps + 1
        # remove 1 at the end, so a->b->c yields 2 steps (not 3)
        self._n_steps = res - 1
        return self._n_steps

    @property
    def all_nodes(self) -> tuple[str, ...] | tuple[int, ...]:
        """returns all the nodes in this pathway"""
        res = set()
        for node_or_path in self.nodes_and_paths:
            if isinstance(node_or_path, (str, int)):
                res.add(node_or_path)
            else:
                for path in node_or_path:
                    res.update(path.all_nodes)
        return sorted(tuple(res))

    @property
    def all_edges(self) -> list[tuple[str, str]]:
        """returns all the edges in this pathway"""
        from .converging_pathways import ConvergingPathways
        assert isinstance(self.nodes_and_paths[0], (str, int, ConvergingPathways)), self.nodes_and_paths
        # First node can be a CP, so it's treated separately
        if isinstance(self.nodes_and_paths[0], (str, int)):
            res = [self.nodes_and_paths[0: 2]] if len(self.nodes_and_paths) > 1 else []
        else:
            res = []
            for item in self.nodes_and_paths[0]:
                res.extend(item.all_edges)
            if len(self.nodes_and_paths) > 1:
                res.append((self.nodes_and_paths[0].converging_node, self.nodes_and_paths[1]))

        for left, right in zip(self.nodes_and_paths[1: -1], self.nodes_and_paths[2:]):
            assert isinstance(left, (str, int)), left
            assert isinstance(right, (str, int)), right
            res.append((left, right))

        res = sorted(set(res))
        return res

    # Public methods

    def is_line_pathway(self) -> bool:
        """returns true if this pathway is linear"""
        from .converging_pathways import ConvergingPathways
        for node_or_path in self.nodes_and_paths:
            if isinstance(node_or_path, ConvergingPathways):
                return False
            if isinstance(node_or_path, Pathway):
                return node_or_path.is_line_pathway()
        return True

    def has_output_edge(self) -> bool:
        """
        Returns true if the pathway has an output edge
        Okay: P(a->b) and P(CP(a->x, b->x)->y)
        Not okay: P(a) and PCP(a->x, b->x))
        """
        return isinstance(self.nodes_and_paths[-1], (str, int)) and len(self.all_nodes) > 1

    def check_pathway(self, graph: Graph):
        """checks the pathway is valid for the given graph"""
        for node_or_path in self.nodes_and_paths:
            assert isinstance(node_or_path, (list, tuple, int, str)), (node_or_path, type(node_or_path))
            if isinstance(node_or_path, (list, tuple)):
                assert len(node_or_path) > 1
                last_node = node_or_path[0].nodes_and_paths[-1]
                for inner_path in node_or_path:
                    assert isinstance(inner_path, Pathway), (inner_path, type(inner_path))
                    inner_path.check_pathway(graph)
                    p_last_node = inner_path.nodes_and_paths[-1]
                    assert p_last_node == last_node, f"List paths have different nodes: {p_last_node} vs {last_node}"
                continue

            if node_or_path not in graph.node_names:
                raise ValueError(f"Node '{node_or_path}' of path: '{self}' not found in the graph")

    def to_graphviz(self, t: int = None) -> Digraph:
        """Returns a graphviz object from this path. Used for plotting the graph. Best for smaller graphs."""
        from .converging_pathways import ConvergingPathways
        g = Digraph()
        g.attr(rankdir="LR")
        t = self.delay if t is None else t

        # only the first item can be a ConvergingPathway
        nodes_and_paths = list(self.nodes_and_paths)
        if isinstance(nodes_and_paths[0], ConvergingPathways):
            g2 = nodes_and_paths[0].to_graphviz(t)
            g2.name = "cluster_0"
            g.subgraph(g2)
            t += nodes_and_paths[0].n_steps
            nodes_and_paths[0] = nodes_and_paths[0].converging_node

        for i in range(len(nodes_and_paths) - 1):
            l, r = nodes_and_paths[i], nodes_and_paths[i + 1]
            assert isinstance(l, (int, str)), l
            assert isinstance(r, (int, str)), r
            g.edge(f"{l}", f"{r}", label=f"t={t + i}")
        return g

    # Private methods

    def _build_nodes_and_paths(self, nodes_and_paths: list["ConvergingPathways" | str | int]) -> tuple:
        from .converging_pathways import ConvergingPathways
        # First item in a pathway may also be a ConvergingPathways object
        for i, item in enumerate(nodes_and_paths):
            assert isinstance(item, (str, int)) or (isinstance(item, ConvergingPathways) and i == 0), item
        return tuple(nodes_and_paths)

    def _build_partial_pathways(self) -> list[Pathway]:
        res = set()
        from .converging_pathways import ConvergingPathways
        if isinstance(self.nodes_and_paths[0], ConvergingPathways):
            res.update(self.nodes_and_paths[0].partial_pathways)
        for i in range(1, len(self) + 1):
            res.add(Pathway(self.nodes_and_paths[0:i]))
        res = sorted(res)
        return res

    def _check_pathway(self):
        """
        Check for repeated sequential nodes in a pathway [a->b->b->c].
        In theory these could be okay (autoencoder for the node), but in most cases it's a mistake.
        We can explicitly create a subclass of Pathway to allow these later on.
        """
        from .converging_pathways import ConvergingPathways
        first_ix = 0 if not isinstance(self.nodes_and_paths[0], ConvergingPathways) else 1
        assert isinstance(self.nodes_and_paths[0], (str, int, ConvergingPathways)), self.nodes_and_paths
        if len(self.nodes_and_paths) == first_ix:
            return
        prev_node = self.nodes_and_paths[first_ix]
        for i in range(first_ix + 1, len(self.nodes_and_paths)):
            assert isinstance(self.nodes_and_paths[i], (str, int))
            current_node = self.nodes_and_paths[i]
            assert prev_node != current_node, f"Pathway has repeated node: {self}. Node '{prev_node}'"
            prev_node = current_node

    def __hash__(self):
        return hash(self.nodes_and_paths)

    def __len__(self):
        return len(self.nodes_and_paths)

    def __lt__(self, other: Pathway):
        if isinstance(other, tuple):
            return self < Pathway(other)
        return len(self.nodes_and_paths) < len(other.nodes_and_paths)

    def __eq__(self, other: str | Pathway | tuple[str, ...] | tuple[int, ...]):
        if isinstance(other, (tuple, list, str, int)):
            return self == Pathway(other)
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __str__(self):
        nodes = '->'.join(str(n) for n in self.nodes_and_paths)
        delay_str = f";d={self.delay}" if self.delay else ""
        return f"P({nodes}{delay_str})"

    def __repr__(self):
        nodes = "->".join(repr(n) for n in self.nodes_and_paths)
        delay_str = f";d={self.delay}" if self.delay else ""
        return f"{Fore.GREEN}P({Style.RESET_ALL}{nodes}{delay_str}{Fore.GREEN}){Style.RESET_ALL}"

    def __getitem__(self, index: int):
        return self.nodes_and_paths[index]
