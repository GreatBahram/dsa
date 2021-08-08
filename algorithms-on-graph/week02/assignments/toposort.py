"""Find a topological sort of a given directed graph."""
from collections import deque


class DirGraph:
    def __init__(self, vertices):
        self.adj = {}
        for v in vertices:
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1, v2):
        self.adj[v1].append(v2)

    def topological_sort(self) -> bool:
        visited = set()
        stack = deque()
        for v in self.adj:
            if v not in visited:
                self.explore(v, visited, stack)
        return stack

    def explore(self, vertex, visited: set, stack: deque) -> bool:
        visited.add(vertex)
        for child in self.adj[vertex]:
            if child not in visited:
                self.explore(child, visited, stack)
        stack.appendleft(vertex)

    @classmethod
    def from_edges(cls, vertices, edges):
        graph = cls(vertices)
        for v1, v2 in edges:
            graph.add(v1, v2)
        return graph


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    graph = DirGraph.from_edges(range(1, n_vertices + 1), edges)
    print(*graph.topological_sort())
