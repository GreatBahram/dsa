import math
import queue
from numbers import Number
from typing import NamedTuple


class WeightedEdge(NamedTuple):
    u: int
    v: int
    weight: Number


class DirGraph:
    """
    Directed graph using adjacency list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adj = {}
        for v in range(vertices + 1):
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({self.edges})>"

    def add(self, u: int, v: int, weight: Number) -> None:
        self.adj[u].append(WeightedEdge(u, v, weight))

    def compute_spt(self, src) -> dict:
        """
        It uses bellman-ford algorirthm and infinite arbitrage alg
        to compute the shortest path from a given src.
        Runnig time: O(|V||E|)
        A given graph might be **disconnected** so we should make sure
        we traverse all disconnected components.
        """
        distances = {v: math.inf for v in range(self.vertices + 1)}
        distances[src] = 0

        # A simple Bellman-Ford
        for _ in range(self.vertices):
            for vertex in range(self.vertices + 1):
                for u, v, weight in self.adj[vertex]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # check for negative cycle
        q = queue.Queue()
        visited = set()

        # find all nodes that changed the on the V iteration
        for vertex in range(self.vertices + 1):
            for u, v, weight in self.adj[vertex]:
                if distances[u] + weight < distances[v]:
                    q.put(v)

        # Perform a BFS ordering
        while not q.empty():
            u = q.get()
            if u not in visited:
                visited.add(u)
                distances[u] = -math.inf
                for _, child, _ in self.adj[u]:
                    if child not in visited:
                        q.put(child)
        return distances


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    src = int(input())
    dir_graph = DirGraph(n_vertices)
    for v1, v2, weight in edges:
        dir_graph.add(v1, v2, weight)
    spt = dir_graph.compute_spt(src)
    mapping = {math.inf: "*", -math.inf: "-"}
    for v in range(1, n_vertices + 1):
        spt_value = spt[v]
        print(mapping.get(spt_value, spt_value))
