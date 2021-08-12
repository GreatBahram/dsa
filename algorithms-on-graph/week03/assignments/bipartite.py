"""Breadth-first search to find out whether a graph is bipartite or not."""
import random
from queue import Queue

RED = 0
BLUE = 1


class Graph:
    """Undirected graph Adjacency list representation."""

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        for v in vertices:
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def _is_bipartite(self, origin, visited):
        q = Queue()
        color_map = {origin: RED}
        q.put(origin)
        visited.add(origin)

        while not q.empty():
            node = q.get()
            for child in self.adj[node]:
                if child not in color_map:
                    color_map[child] = RED if color_map[node] == BLUE else BLUE
                    visited.add(child)
                    q.put(child)
                else:
                    if color_map[child] == color_map[node]:
                        return False
        return True

    def is_bipartite(self) -> bool:
        """I used two is_bipartitle because the given graph have more than one
        connected components, i.e it has disconnected nodes."""
        visited = set()
        for vertex in self.adj:
            if vertex not in visited:
                if self._is_bipartite(vertex, visited) is False:
                    return False
        return True

    @classmethod
    def from_edges(cls, vertices, edges):
        graph = cls(vertices)
        for v1, v2 in edges:
            graph.add(v1, v2)
        return graph


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    graph = Graph.from_edges(range(1, n_vertices + 1), edges)
    print(int(graph.is_bipartite()))
