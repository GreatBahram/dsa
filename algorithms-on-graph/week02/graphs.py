from collections import defaultdict, deque
from collections.abc import Sequence


class AdjacencyList:
    def __init__(self, n_vertices: int) -> None:
        self.adj = defaultdict(list)
        for i in range(1, n_vertices + 1):
            self.adj[i]

    def add(self, v1, v2) -> None:
        self.adj[v1].append(v2)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(dict(self.adj))})"


# topological sort
class Graph(AdjacencyList):
    """
    >>> g = Graph(4)
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
class Graph(AdjacencyList):
    """
    >>> g = Graph(4)
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
