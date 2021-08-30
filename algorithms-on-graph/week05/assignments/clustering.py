"""Implementing the minimum spanning tree using Kruskal's algorithm."""
import math
from typing import NamedTuple, Set


class Point(NamedTuple):
    x: int
    y: int


def euclidean_distance(p1: Point, p2: Point) -> float:
    """Calculate the Euclidean distance between two given points."""
    xdist = p1.x - p2.x
    ydist = p1.y - p2.y
    return math.sqrt((xdist * xdist) + (ydist * ydist))


class Edge(NamedTuple):
    i: int
    j: int
    distance: float

    def __lt__(self, other):
        return self.distance < other.distance


class UnionFind:
    """
    Naive Disjoint-Set implementation.
    """

    def __init__(self, maxsize: int):
        self._container = list(range(maxsize + 1))

    def find(self, item_a, item_b) -> bool:
        """Return True if item_a and item_b belong to the same set."""
        root_a = self.root(item_a)
        root_b = self.root(item_b)
        return root_a == root_b

    def union(self, item_a, item_b) -> None:
        """Attach the roots of item_a and item_b."""
        root_a = self.root(item_a)
        root_b = self.root(item_b)

        if root_a == root_b:
            return None

        # this operation takes O(n)
        for item_idx, parent_ref in enumerate(self._container):
            if parent_ref == root_a:
                self._container[item_idx] = root_b

    def root(self, item) -> int:
        while item != self._container[item]:
            item = self._container[item]
        return item

    @property
    def clusers(self) -> int:
        """Return the number of sets."""
        return len(set(self._container))

    def __repr__(self):
        return f"{type(self).__name__}({self._container!r})"


class Graph:
    def __init__(self, n_vertices, edges):
        self.uf = UnionFind(n_vertices)
        self.edges = edges

    def perform_clustering(self, k: int) -> Set[Edge]:
        """
        Perform max spacing for k order cluster using kruskal's
        algorithm
        """
        sorted_edges = sorted(self.edges)
        chosen_edges = set()
        last_distance = -1
        for edge in sorted_edges:
            if self.uf.clusers == k:
                break
            u, v, _ = edge
            if not self.uf.find(u, v):
                self.uf.union(u, v)
                chosen_edges.add(edge)
                last_distance = edge.distance
        return last_distance


if __name__ == "__main__":
    n_points = int(input())
    points = [Point(*map(int, input().split())) for _ in range(n_points)]
    k = int(input())
    edges = []
    for i_idx, p1 in enumerate(points):
        for j_idx, p2 in enumerate(points[i_idx + 1 :], i_idx + 1):
            e = Edge(i_idx, j_idx, euclidean_distance(p1, p2))
            edges.append(e)
    graph = Graph(n_points, edges)
    print(f"{graph.perform_clustering(k):.9f}")
