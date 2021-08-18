import math
from numbers import Number
from typing import NamedTuple


class WeightedEdge(NamedTuple):
    u: int
    v: int
    weight: Number


class DirGraph:
    """
    Directed graph using edge list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({self.edges})>"

    def add(self, u: int, v: int, weight: Number):
        self.edges.append(WeightedEdge(u, v, weight))

    def bellman_ford(self, src, distances):
        distances[src] = 0

        for _ in range(self.vertices):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # check for negative cycle
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                return True
        return False

    def has_negative_cycle(self, src=1) -> bool:
        """
        Runnig time: O(|V||E|)
        A given graph might be **disconnected** so we should make sure
        we traverse all disconnected components.
        """
        visited = set()
        distances = {v: math.inf for v in range(self.vertices + 1)}
        for vertex in range(self.vertices + 1):
            if vertex not in visited:
                if self.bellman_ford(vertex, distances):
                    return True
                # mark all vertices with noninfinite weight as visited
                for v, weight in distances.items():
                    if not math.isinf(weight):
                        visited.add(v)
        return False


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    dir_graph = DirGraph(n_vertices)
    for v1, v2, weight in edges:
        dir_graph.add(v1, v2, weight)
    print(int(dir_graph.has_negative_cycle()))
