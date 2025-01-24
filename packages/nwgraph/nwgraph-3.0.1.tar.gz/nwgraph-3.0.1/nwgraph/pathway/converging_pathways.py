"""ConvergingPathways module"""
# pylint: disable=import-outside-toplevel
from __future__ import annotations
from colorama import Fore, Style
from graphviz import Digraph

class ConvergingPathways:
    """ConvergingPathways implementation. This is a list of pathways that converge into a single node."""
    def __init__(self, paths: list["Pathway"] | tuple["Pathway", ...], add_delays: bool = False):
        self.add_delays = add_delays
        self.paths: tuple["Pathway", ...] = self._build_cp(paths)
        self._partial_pathways: list["Pathway"] | None = None
        self._n_steps: int | None = None
        self._check_pathway()

    def _build_cp(self, paths: list["Pathway"] | tuple["Pathway", ...]) -> tuple["Pathway", ...]:
        from .pathway import Pathway
        assert len(paths) > 1, f"pathways must be non-empty and contain at least 2 items: {paths}"
        assert isinstance(paths[0][-1], (str, int)), f"Last node is not a string or int, got {paths[0][-1]}"
        if not all(isinstance(p, Pathway) for p in paths):
            raise TypeError(f"paths must be Pathway objects, got {paths}")
        if not all(p[-1] == paths[0][-1] for p in paths):
            raise ValueError(f"Last node must be the same: {paths}")

        n_steps = [p.n_steps for p in paths]
        if not all(x == n_steps[0] for x in n_steps):
            if not self.add_delays:
                raise ValueError(f"Number of steps must be the same: {[f'{p}=>{p.n_steps}' for p in paths]}")

            # We add the delay to the converging pathway
            new_paths = []
            for p in paths:
                new_paths.append(Pathway(p.nodes_and_paths, delay=n_steps[0] - p.n_steps))
            paths = new_paths

        return tuple(paths)

    @property
    def converging_node(self):
        """returns the converging node"""
        return self.paths[0][-1]

    @property
    def n_steps(self) -> int:
        """Get the number of steps in the pathway list"""
        if self._n_steps is not None:
            return self._n_steps
        self._n_steps = max(p.n_steps for p in self.paths)
        return self._n_steps

    def to_graphviz(self, t: int = None) -> Digraph:
        """Converts the ConvergingPathways object to a graphviz object"""
        t = 0 if t is None else t
        g = Digraph()
        g.attr(rankdir="LR")
        for pathway in self.paths:
            g.subgraph(pathway.to_graphviz(t + pathway.delay))
        return g

    @property
    def partial_pathways(self) -> list["Pathway"]:
        """
        Given a list of pathways, merge their partial pathways into a single list. Common paths are put only once.
        Example:
            pathways = [
                ("a", "b", "c", "d"),
                ("a", "b", "d", "c", "e"),
                ("a", "b", "c", "e"),
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
        for pathway in self.paths:
            res.update(pathway.partial_pathways)
        # sort first by length of the path, then by lexicographical order
        self._partial_pathways = sorted(res)
        return self._partial_pathways

    def _check_pathway(self):
        pass

    def __hash__(self):
        return hash(self.paths)

    def __eq__(self, other: str | ConvergingPathways | tuple[str, ...] | tuple[int, ...]):
        if isinstance(other, (tuple, list)):
            other = ConvergingPathways(other)
        if not isinstance(other, ConvergingPathways):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, index: int):
        return self.paths[index]

    def __str__(self) -> str:
        paths = '|'.join(str(p) for p in self.paths)
        return f"CP{{{paths}}}"

    def __repr__(self) -> str:
        paths = f"{Fore.YELLOW}|{Style.RESET_ALL}".join(repr(p) for p in self.paths)
        return f"{Fore.YELLOW}CP{{{Style.RESET_ALL}{paths}{Fore.YELLOW}}}{Style.RESET_ALL}"
