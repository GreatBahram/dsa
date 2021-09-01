from typing import List


class Graph:
    """Undirected graph using adjacency list representation."""

    def __init__(self, number_of_vertices: int) -> None:
        self.adj = {}

        for v in range(1, number_of_vertices + 1):
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(dict(self.adj))})"

    def add(self, vertex1, vertex2) -> None:
        self.adj[vertex1].append(vertex2)
        self.adj[vertex2].append(vertex1)

    def update(self, edges) -> None:
        """Update the graph by a given list of edges."""
        for v1, v2 in edges:
            self.add(v1, v2)

    def get_connected_components(self) -> List[List[int]]:
        visited = set()
        cc = []

        for vertex in self.adj:
            if vertex not in visited:
                temp = []
                cc.append(self.explore(vertex, visited, temp))
        return cc

    def explore(self, vertex, visited, temp) -> List[List[int]]:
        visited.add(vertex)
        temp.append(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                temp = self.explore(neighbor, visited, temp)
        return temp


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    graph = Graph(n)
    graph.update(edges)

    print(len(graph.get_connected_components()))
