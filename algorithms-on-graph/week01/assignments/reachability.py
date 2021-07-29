from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices: int) -> None:
        self.adj = defaultdict(list)

        for v in range(1, number_of_vertices + 1):
            self.adj[v]

    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(dict(self.adj))})"

    def add(self, vertex1, vertex2) -> None:
        self.adj[vertex1].append(vertex2)
        self.adj[vertex2].append(vertex1)

    def update(self, edges) -> None:
        """Update the graph by a given list of edges."""
        for v1, v2 in edges:
            self.add(v1, v2)

    def is_connected(self, v1, v2) -> None:
        """
        Return True if there is a connection; False otherwise.
        """
        # if it is connected directly, then don't search for it.
        if v2 in self.adj[v1]:
            return True

        visited = set()
        self.explore(v1, visited)
        return v2 in visited

    def explore(self, vertex1, visited: set) -> None:
        visited.add(vertex1)
        for neighbor in self.adj[vertex1]:
            if neighbor not in visited:
                self.explore(neighbor, visited)
        return None


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    query_vertices = list(map(int, input().split()))

    graph = Graph(n)
    graph.update(edges)

    print(int(graph.is_connected(*query_vertices)))
