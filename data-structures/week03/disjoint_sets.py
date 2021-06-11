from abc import ABC, abstractmethod


class BaseUnionFind(ABC):
    @abstractmethod
    def find(self, item_a, item_b) -> bool:
        """Return True if item_a and item_b belong to the same set."""
        pass

    @abstractmethod
    def union(self, item_a, item_b) -> None:
        """Attach the roots of item_a and item_b."""
        pass


class NaiveUnionFind(BaseUnionFind):
    """
    We call this implementation Naive, because:
    * find operation will find the root of the node recursively
      and after that it won't store that information for later usage.

    * union operation does not take the size of each subtree into consideration
      to decrease the height of the tree.
    """

    def __init__(self, maxsize: int) -> None:
        self._container = list(range(maxsize + 1))
        self.maxsize = maxsize

    def root(self, item):
        while item != self._container[item]:
            item = self._container[item]
        return item

    def find(self, item_a, item_b) -> bool:
        root_a = self.root(item_a)
        root_b = self.root(item_b)
        return root_a == root_b

    def union(self, item_a, item_b) -> None:
        root_a = self.root(item_a)
        root_b = self.root(item_b)
        if root_a == root_b:
            return None

        # this operation takes O(n)
        for item_idx, parent_ref in enumerate(self._container):
            if parent_ref == root_a:
                self._container[item_idx] = root_b


class UnionFind(BaseUnionFind):
    def __init__(self, maxsize: int):
        self._container = list(range(maxsize + 1))
        self.maxsize = maxsize
        # size holds the height of each subtree
        self.size = [0] * maxsize

    def __repr__(self):
        return f"{type(self).__name__}({self._container!r})"

    def union(self, a: int, b: int) -> None:
        """
        Union by rank/size

        The union by size/rank heuristic guarantees that
        union and find methods work in time O(\\lg n).

        Before connecting two sub-tree, it checks the size of them
        and connect the smaller one to the larger one.
        """
        root_a = self.root(a)
        root_b = self.root(b)

        # if they already have a connection give up.
        if root_a == root_b:
            return None

        if self.size[root_a] > self.size[root_b]:
            self._container[root_b] = root_a
        else:
            self._container[root_a] = self._container[root_b]
            if self.size[root_a] == self.size[root_b]:
                self.size[root_b] = self.size[root_b] + 1

    def find(self, a: int, b: int) -> bool:
        return self.root(a) == self.root(b)

    def root(self, item: int) -> int:
        """
        return the root of a given item and also use the path comprehension
        to decrease the depth of tree significantly, which results in log* n for
        find and union operations.
        """
        if self._container[item] != item:
            self._container[item] = self.root(self._container[item])
        return self._container[item]
