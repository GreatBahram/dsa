from collections import defaultdict, deque
from collections.abc import Sequence
from typing import TypeVar

V = TypeVar("V")


class AdjacencyList:
    def __init__(self, vertices: list[V]) -> None:
        self.vertices = vertices
        self.adj = defaultdict(list)
        for v in vertices:
            self.adj[v]

    def add(self, v1, v2) -> None:
        self.adj[v1].append(v2)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(dict(self.adj))})"

    @classmethod
    def from_edges(cls, vertices, edges):
        g = cls(vertices)
        for v1, v2 in edges:
            g.add(v1, v2)
        return g


# topological sort
class Graph(AdjacencyList):
    """
    >>> g = Graph([1, 2, 3, 4])
    >>> g.add(1, 2)
    >>> g.add(1, 3)
    >>> g.add(3, 4)
    >>> g.topological_sort()
    deque([1, 3, 4, 2])
    """

    def explore(self, vertex, visited, stack):
        visited.add(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self.explore(neighbor, visited, stack)

        stack.appendleft(vertex)

    def topological_sort(self) -> Sequence:
        visited = set()
        stack = deque()

        for vertex in self.adj:
            if vertex not in visited:
                self.explore(vertex, visited, stack)
        return stack


# Strongly connected components, Naive and efficient algorithm
class Graph2(AdjacencyList):
    """
    >>> g = Graph2.from_edges([0, 1, 2, 3, 4], [(0, 2), (1, 0), (2, 1), (0, 3), (3, 4)])
    >>> g.scc()
    [[0, 1, 2], [3], [4]]
    """

    def fill_order(self, vertex, visited, stack):
        visited.add(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self.fill_order(neighbor, visited, stack)

        stack.append(vertex)

    def scc(self):
        """Return a list of all strongly connected components."""
        # calculate vertices sorted by reverse postorder time
        visited = set()
        stack = []

        for vertex in self.adj:
            if vertex not in visited:
                self.fill_order(vertex, visited, stack)

        # get a reversed graph
        rev_graph = self.reversed()

        # calculate the scc
        visited = set()
        cc = []

        for v in reversed(stack):
            if v not in visited:
                temp = []
                cc.append(rev_graph.explore(v, visited, temp))
        return cc

    def explore(self, v, visited, temp):
        """this a normal DFS."""
        visited.add(v)
        temp.append(v)

        for neighbor in self.adj[v]:
            if neighbor not in visited:
                temp = self.explore(neighbor, visited, temp)
        return temp

    def reversed(self):
        """Return a reversed graph of the current graph"""
        g = type(self)(self.vertices)
        for v, neighbors in self.adj.items():
            for n in neighbors:
                g.add(n, v)
        return g
