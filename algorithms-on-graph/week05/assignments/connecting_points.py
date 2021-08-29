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
    Disjoint-Set implementation using union by rank and 
    path compression to make it faster.
    """
    def __init__(self, maxsize: int):
        self._container = list(range(maxsize + 1))
        self.maxsize = maxsize
        self.size = [1] * (maxsize + 1)

    def find(self, item_a, item_b) -> bool:
        """Return True if item_a and item_b belong to the same set."""
        root_a = self.root(item_a)
        root_b = self.root(item_b)
        return root_a == root_b

    def union(self, item_a, item_b) -> None:
        """Attach the roots of item_a and item_b, take size into
        consideration."""
        root_a = self.root(item_a)
        root_b = self.root(item_b)

        if root_a == root_b:
            return None

        if self.size[root_a] < self.size[root_b]:
            self._container[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self._container[root_b] = root_a
            self.size[root_a] += self.size[root_b]

    def root(self, item) -> int:
        """This is where path compression happens"""
        while self._container[item] != item:
            self._container[item] = self._container[self._container[item]]
            item = self._container[item]
        return item

    def __repr__(self):
        return f"{type(self).__name__}({self._container!r})"


class Graph:
    def __init__(self, n_vertices, edges):
        self.edges = edges
        self.uf = UnionFind(n_vertices)

    def kruskal(self) -> Set[Edge]:
        """
        Return the minimum cost for constructing a minimum spanning tree using
        kruskal's algorithm.
        """
        sorted_edges = sorted(self.edges)
        chosen_edges = set()
        for edge in sorted_edges:
            u, v, _ = edge
            if not self.uf.find(u, v):
                self.uf.union(u, v)
                chosen_edges.add(edge)
        return sum(e.distance for e in chosen_edges)


if __name__ == "__main__":
    n_points = int(input())
    points = [Point(*map(int, input().split())) for _ in range(n_points)]
    edges = []
    for i_idx, p1 in enumerate(points):
        for j_idx, p2 in enumerate(points[i_idx + 1 :], i_idx + 1):
            e = Edge(i_idx, j_idx, euclidean_distance(p1, p2))
            edges.append(e)
    print(edges)
    graph = Graph(n_points, edges)
    print(f"{graph.kruskal():.9f}")
