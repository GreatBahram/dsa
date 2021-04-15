class UnionFind:
    def __init__(self, n: int):
        self.container = list(range(n + 1))
        self.size = [0] * n

    def __repr__(self):
        return f"{type(self).__name__}({self.container!r})"

    def simple_union(self, a: int, b: int) -> None:
        """provide a connection between given two items."""
        root_a = self.root(a)
        root_b = self.root(b)
        self.container[root_a] = self.container[root_b]

    def union(self, a: int, b: int) -> None:
        """weighted union."""
        root_a = self.root(a)
        root_b = self.root(b)
        # if they already have a connection give up.
        if root_a == root_b:
            return None

        # = means default assignment is from left to right
        if self.size[a] <= self.size[b]:
            self.container[root_a] = self.container[root_b]
            self.size[b] += 1
        else:
            self.container[root_b] = self.container[root_a]
            self.size[a] += 1

    def find(self, a: int, b: int) -> bool:
        return self.root(a) == self.root(b)

    def simple_root(self, item: int) -> int:
        """return the root of a given item."""
        while self.container[item] != item:
            item = self.container[item]
        return item

    def root(self, item: int) -> int:
        """return the root of a given item and also use path comprehension."""
        if self.container[item] != item:
            self.container[item] = self.root(self.container[item])
        return self.container[item]
