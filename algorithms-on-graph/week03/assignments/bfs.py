"""Breadth-first search ordering"""
from queue import Queue


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

    def bfs(self, origin, destination):
        """
        Run breadth-first ordering and return a parent-child mapping or
        shortest path tree."""
        queue = Queue()
        queue.put(origin)
        visited = {origin}
        prev = dict(origin=None)

        while not queue.empty():
            node = queue.get()
            for nxt in self.adj[node]:
                if nxt not in visited:
                    queue.put(nxt)
                    visited.add(nxt)
                    prev[nxt] = node

        return prev

    def distance(self, s, t):
        shortest_path_tree = self.bfs(s, t)
        path = self.reconstruct_path(s, t, shortest_path_tree)
        return path

    def reconstruct_path(self, origin, dest, prev_map: dict):
        try:
            array = []
            while dest != origin:
                array.append(dest)
                dest = prev_map[dest]
            return array[::-1]
        except KeyError:
            return []

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
    s, t = map(int, input().split())
    path = graph.distance(s, t)
    print(-1 if not path else len(path))
