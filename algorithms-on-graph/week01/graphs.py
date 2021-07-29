from collections import defaultdict
from typing import TypeVar

Vertex = TypeVar("Vertex")


class AdjacencyList:
    def __init__(self):
        self.adj = defaultdict(list)

    def __repr__(self):
        return repr(dict(self.adj))

    def add(self, v: Vertex, w: Vertex) -> None:
        """Add an edge from v to w and vice versa."""
        self.adj[v].append(w)
        self.adj[w].append(v)

    @classmethod
    def from_edges(cls, list_of_edges: list[tuple[Vertex, Vertex]]) -> "AdjacencyList":
        graph = cls()
        for v1, v2 in list_of_edges:
            graph.add(v1, v2)
        return graph


# calculate the number of connected components
class Graph(AdjacencyList):
    """
    >>> g = Graph()
    >>> g.add('a', 'b')
    >>> g.add('a', 'c')
    >>> g.add('d', 'e')
    >>> len(g.get_connected_components())
    2
    """

    def get_connected_components(self) -> list[list[Vertex]]:
        visited = set()
        cc = []
        for vertex in self.adj:
            if vertex not in visited:
                temp = []
                cc.append(self.explore(vertex, visited, temp))
        return cc

    def explore(self, vertex, visited: dict, temp: list):
        visited.add(vertex)
        temp.append(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                temp = self.explore(neighbor, visited, temp)
        return temp


# Checking whether there is a path between the given two vertices
class Graph2(AdjacencyList):
    """
    >>> g = Graph2()
    >>> g.add('a', 'b')
    >>> g.add('b', 'c')
    >>> g.add('d', 'e')
    >>> g.is_connected('a', 'c')
    True
    >>> g.is_connected('b', 'e')
    False
    """

    def explore(self, vertex, visited: dict):
        """DFS implementation"""
        visited.add(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self.explore(neighbor, visited)

    def is_connected(self, vertex1, vertex2) -> bool:
        visited = set()
        self.explore(vertex1, visited)
        return vertex2 in visited


# checking whether there is a cycle
class Graph3(AdjacencyList):
    """
    You might find the explanation of this video beneficial
    >>> g = Graph3()
    >>> g.add('a', 'b')
    >>> g.add('b', 'c')
    >>> g.add('c', 'd')
    >>> g.add('b', 'd')
    >>> g.is_cyclic()
    True
    """

    def explore(self, vertex, visited: set, parent):
        """
        Using DFS algorithm look for back-edge
        A Back Edge is an edge that connects a vertex to a vertex that is
        discovered before it's parent.
        """
        visited.add(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                if self.explore(neighbor, visited, vertex):
                    return True
            else:
                # if it has been visited, check whether it is our
                # parent or not, if it isn't, then it is a back edge.
                if neighbor != parent:
                    return True
        return False

    def is_cyclic(self) -> bool:
        visited = set()

        for vertex in self.adj:
            if vertex not in visited:
                if self.explore(vertex, visited, -1):
                    return True
        return False

    def get_cycle_path(self) -> str:
        if not self.is_cyclic():
            return ""

        temp = []
        visited = set()

        for vertex in self.adj:
            if vertex not in visited:
                self._explore(vertex, visited, -1, temp)
        return " -> ".join(map(str, temp))

    def _explore(self, vertex, visited, parent, temp) -> bool:
        visited.add(vertex)
        temp.append(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                if self._explore(neighbor, visited, vertex, temp):
                    return True
            else:
                if neighbor != parent:
                    temp.append(neighbor)
                    return True
        return False
