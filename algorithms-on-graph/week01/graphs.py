from collections import defaultdict
from typing import TypeVar

Vertex = TypeVar("Vertex")


# calculate the number of connected components
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def __repr__(self):
        return repr(dict(self.adj))

    def add(self, v: Vertex, w: Vertex) -> None:
        """Add an edge from v to w and vice versa."""
        self.adj[v].append(w)
        self.adj[w].append(v)

    def get_connected_components(self) -> list[list[Vertex]]:
        visited = dict.fromkeys(self.adj, False)
        cc = []
        for vertex in self.adj:
            if not visited[vertex]:
                temp = []
                cc.append(self.explore(vertex, visited, temp))
        return cc

    def explore(self, vertex, visited: dict, temp: list):
        visited[vertex] = True
        temp.append(vertex)
        for neighbor in self.adj[vertex]:
            if not visited[neighbor]:
                temp = self.explore(neighbor, visited, temp)
        return temp


# Checking whether there is a path between the given two vertices
class Graph2:
    def __init__(self):
        self.adj = defaultdict(list)

    def __repr__(self):
        return repr(dict(self.adj))

    def add(self, v: Vertex, w: Vertex) -> None:
        """Add an edge from v to w and vice versa."""
        self.adj[v].append(w)
        self.adj[w].append(v)

    def explore(self, vertex, visited: dict):
        """DFS implmentation"""
        visited[vertex] = True
        for neighbor in self.adj[vertex]:
            if not visited[neighbor]:
                self.explore(neighbor, visited)

    def find_path(self, vertex1, vertex2) -> bool:
        visited = dict.fromkeys(self.adj, False)
        self.explore(vertex1, visited)
        return vertex2 in (v for v, is_visited in visited.items() if is_visited)
