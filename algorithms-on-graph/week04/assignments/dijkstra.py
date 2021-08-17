import math
from numbers import Number
from queue import PriorityQueue

NOT_FOUND: int = -1


class DirGraph:
    """
    Directed graph using matrix list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = vertices + 1

        self.adj = [[0] * self.vertices for i in range(self.vertices)]

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1: int, v2: int, weight: Number):
        self.adj[v1][v2] = weight

    def distance(self, source: int, destination: int) -> int:
        """
        Compute the weight of a shortest path between source and destination.
        Return NOT_FOUND if there is path
        """
        shortest_path_map = self.dijkstra(source)
        weight = shortest_path_map.get(destination)
        return NOT_FOUND if math.isinf(weight) else weight

    def dijkstra(self, src: int):
        """
        This dijkstra is implemented using an array which results in
        O(V ** 2) running time, this can be improved using a priority queue.
        """
        distances = {v: math.inf for v in range(self.vertices)}
        distances[src] = 0
        visited = set()

        for _ in range(self.vertices):
            u = self.min_distances(distances, visited)
            visited.add(u)

            for v, weight in enumerate(self.adj[u]):
                is_visited = v in visited
                has_connection = weight > 0
                if is_visited or not has_connection:
                    continue

                new_path = distances[u] + self.adj[u][v]
                is_shorter_path = new_path < distances[v]

                if is_shorter_path:
                    distances[v] = new_path
        return distances

    def min_distances(self, distances, visited: set) -> int:
        """return the index of minimum wieght inside distances"""
        distances = distances.copy()
        for v in visited:
            distances.pop(v)
        return min(distances, key=lambda v: distances[v])


class WeightedEdge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __iter__(self):
        yield from (self.vertex, self.weight)

    def __repr__(self):
        return f"(v={self.vertex}, w={self.weight})"


class DirGraph:
    """
    Directed graph using adjacency list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = vertices + 1
        self.adj = {}
        for v in range(self.vertices):
            self.adj[v] = []
        # self.adj = [[0] * self.vertices for i in range(self.vertices)]

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1: int, v2: int, weight: Number):
        # self.adj[v1][v2] = weight
        self.adj[v1].append(WeightedEdge(v2, weight))

    def distance(self, source: int, destination: int) -> int:
        """
        Compute the weight of a shortest path between source and destination.
        Return NOT_FOUND if there is path
        """
        shortest_path_map = self.dijkstra(source)
        weight = shortest_path_map.get(destination)
        return NOT_FOUND if math.isinf(weight) else weight

    def dijkstra(self, src: int):
        """
        This dijkstra is implemented using a priority queue results in
        O(|V| + |E| log |V|) running time, this can be improved using a priority queue.
        """
        distances = {v: math.inf for v in range(self.vertices)}
        distances[src] = 0
        visited = set()

        pq = PriorityQueue()
        for v in range(self.vertices):
            pq.put((math.inf, v))

        pq.put((0, src))

        while not pq.empty():
            weight, u = pq.get()
            if math.isinf(weight):  # just to reduce execution time
                continue

            visited.add(u)

            for v, weight in self.adj[u]:
                if v in visited:  # is it visited
                    continue

                new_path = distances[u] + weight
                is_shorter_path = new_path < distances[v]

                if is_shorter_path:
                    distances[v] = new_path
                    pq.put((new_path, v))
        return distances


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    src, dst = map(int, input().split())
    dir_graph = DirGraph(n_vertices)
    for v1, v2, weight in edges:
        dir_graph.add(v1, v2, weight)
    print(dir_graph.distance(src, dst))
