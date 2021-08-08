"""Find a topological sort of a given directed graph."""
import sys

sys.setrecursionlimit(200000)


class DirGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        for v in vertices:
            self.adj[v] = []

    def __repr__(self) -> str:
        return f"<{type(self).__name__}({dict(self.adj)})>"

    def add(self, v1, v2):
        self.adj[v1].append(v2)

    def fill_order(self, vertex, visited: set, stack: list) -> bool:
        visited.add(vertex)
        for child in self.adj[vertex]:
            if child not in visited:
                self.fill_order(child, visited, stack)
        stack.append(vertex)

    def reverse_graph(self):
        rev_graph = type(self)(self.vertices)
        for v, childs in self.adj.items():
            for c in childs:
                rev_graph.add(c, v)
        return rev_graph

    def get_connected_components(self) -> bool:
        # traverse the graph sort item by reverse postorder
        visited = set()
        stack = []
        for v in self.adj:
            if v not in visited:
                self.fill_order(v, visited, stack)

        # generate a reverse graph
        rev_graph = self.reverse_graph()

        # run dfs on the reversed-graph to calculate the connected components
        visited = set()
        cc = []
        for v in reversed(stack):
            if v not in visited:
                temp = []
                cc.append(rev_graph.explore(v, visited, temp))
        return cc

    def explore(self, vertex, visited, temp):
        visited.add(vertex)
        temp.append(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                temp = self.explore(neighbor, visited, temp)
        return temp

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
    print(len(graph.get_connected_components()))
