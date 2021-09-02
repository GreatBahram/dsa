"""Dijkstra's algorithm implementation using both an array and priority queue."""
import math
from dataclasses import dataclass
from queue import PriorityQueue
from typing import Any


class Graph:
    """
    Directed graph using matrix list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = list(range(vertices))
        self.adj = [[0] * vertices for _ in range(vertices)]

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1, v2, weight):
        self.adj[v1][v2] = weight

    def dijkstra(self, source):
        """
        The running time of this algorithm is clearly V^2, because it uses
        a simple array while we could go for a better solution
        using a priority queue.
        """
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[source] = 0

        visited = set()

        for vertex in self.vertices:
            # pick the minimum distance and mark as visited
            u = self.min_distance(distances, visited)
            visited.add(u)

            # Go through all edges of vertex u and do the edge relaxation
            for v in range(self.vertices):
                is_visited = v in visited
                new_path_weight = distances[u] + self.adj[u][v]
                found_shorter_path = distances[v] > new_path_weight
                has_connection = self.adj[u][v] > 0

                if has_connection and not is_visited and found_shorter_path:
                    distances[v] = new_path_weight

        return distances

    def min_distance(self, dist, visited):
        """Return the minimum index"""
        min = math.inf
        for vertex in self.vertices:
            if vertex not in visited and dist[vertex] < min:
                min = dist[vertex]
                min_idx = vertex
        return min_idx


def print_solution(vertices, source, dist):
    print("SRC -> DST: Cost")
    for v in vertices:
        print(f"{source} -> {v}: {dist[v]}")


from queue import PriorityQueue


class Graph2:
    """
    Directed graph using adjacency list representation.
    """

    def __init__(self, vertices: int):
        self.vertices = list(range(vertices))
        self.adj = {}
        for v in self.vertices:
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1, v2, weight):
        self.adj[v1].append((v2, weight))

    def dijkstra(self, source):
        """
        The running time of this algorithm is (|V| + |E| log |V|).
        """
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[source] = 0

        pq = PriorityQueue()
        pq.put((0, source))

        while not pq.empty():
            # extract the vertex with minimum weight and mark as visited
            _, u = pq.get()
            dist_u = distances[u]

            # Go through all edges of vertex u and do the edge relaxation
            for (e, weight) in self.adj[u]:
                is_visited = e in visited
                new_path_weight = distances[u] + self.adj[u][v]
                found_shorter_path = distances[v] > new_path_weight
                has_connection = self.adj[u][v] > 0

                if has_connection and not is_visited and found_shorter_path:
                    distances[v] = new_path_weight

        return distances
