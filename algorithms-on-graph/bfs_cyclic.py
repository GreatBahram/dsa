"""Detect whether there is a cycle inside an undirected graph Using BFS Ordering."""
from queue import Queue


class Graph:
    """Undirected graph using adjacency list representation."""

    def __init__(self, n_vertices: int) -> None:
        self.n_vertices = n_vertices
        self.adj = {}
        for i in range(n_vertices + 1):
            self.adj[i] = []

    def add(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def is_cyclic(self) -> bool:
        """Return True if the graph has a cycle; False otherwise."""
        visited = set()
        for v in range(self.n_vertices + 1):
            if v not in visited and self.explore(v, visited):
                return True
        return False

    def explore(self, vertex, visited: set):
        """Explore the graph using BFS ordering."""
        visited.add(vertex)
        parent = dict.fromkeys(self.adj, -1)
        q = Queue()
        q.put(vertex)
        while not q.empty():
            u = q.get()
            for child in self.adj[u]:
                if child not in visited:
                    visited.add(child)
                    parent[child] = u
                    q.put(child)
                elif child != parent[u]:
                    return True
        return False

    @classmethod
    def from_edges(cls, vertices: int, edges):
        graph = cls(vertices)
        for v1, v2 in edges:
            graph.add(v1, v2)
        return graph
