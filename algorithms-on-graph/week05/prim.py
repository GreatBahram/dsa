"""Implementing the minimum spanning tree using Prim's algorithm."""
import math
from numbers import Number
from queue import PriorityQueue
from typing import NamedTuple, Sequence, Tuple


class WeightedEdge(NamedTuple):
    v: int
    weight: Number

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:
    """Undirected Graph using adjacency list representation."""

    def __init__(self, n_vertices: int) -> None:
        self.n_vertices = n_vertices
        self.adj = {}
        for v in range(n_vertices + 1):
            self.adj[v] = []

    def add(self, v1, v2, weight) -> None:
        self.adj[v1].append((v2, weight))
        self.adj[v2].append((v1, weight))

    def perform_prim(self, starting_vertex):
        cost, parent = {}, {}
        visited = set()
        q = PriorityQueue()

        for v in self.adj:
            cost[v] = math.inf
            parent[v] = None

        cost[starting_vertex] = 0
        q.put(WeightedEdge(starting_vertex, 0))

        while not q.empty():
            v, _ = q.get()
            if v not in visited:
                visited.add(v)
                for neighbor, weight in self.adj[v]:
                    if neighbor not in visited and cost[neighbor] > weight:
                        cost[neighbor] = weight
                        parent[neighbor] = v
                        q.put(WeightedEdge(neighbor, weight))
        return cost, parent

    @classmethod
    def from_edges(
        cls, n_vertices: int, edges: Sequence[Tuple[int, int, Number]]
    ) -> "Graph":
        g = Graph(n_vertices)
        for u, v, w in edges:
            g.add(u, v, w)
        return g
