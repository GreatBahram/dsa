import sys
import threading


class Node:
    def __init__(self, idx=None):
        self.idx = idx
        self.parent = None

    def __repr__(self):
        return f"{type(self).__name__}(index={self.idx}, parent={self.parent})"


class Node2:
    """Each node knows about its children, not its parent."""
    def __init__(self, idx=None):
        self.idx = idx
        self.children = set()

    def __repr__(self):
        return f"{type(self).__name__}(index={self.idx}, children={self.children!r})"


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def find_max_height(node: Node):
    count = 1
    while node.parent is not None:
        node = node.parent
        count += 1
    return count


def max_height(nodes):
    heights = []
    for i in range(len(nodes)):
        heights.append(find_max_height(nodes[i]))
    return max(heights)


def first_approach(n, parents):
    """
    Recursive approach which calculate height for each node
    and then return the maximum one.
    """
    # initialize list of nodes
    nodes = [Node(i) for i in range(n)]

    # connect each node to its parent
    for idx, parent_id in enumerate(parents):
        if parent_id == -1:
            nodes[idx].parent = None
        else:
            nodes[idx].parent = nodes[parent_id]

    print(max_height(nodes))


def second_approach(n, parents):
    """
    In this implementation I went for calculating depth
    from the head node, recursively.
    """
    # initialize list of nodes
    nodes = [Node2(i) for i in range(n)]

    # connect each node to its parent
    for idx, parent_id in enumerate(parents):
        if parent_id == -1:
            head = nodes[idx]
        else:
            nodes[parent_id].children.add(nodes[idx])

    print(compute_depth(head))


def compute_depth(node: Node2):
    if not node.children:
        return 1
    return 1 + max(compute_depth(ch) for ch in node.children)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # print(compute_height(n, parents))
    # first_approach(n, parents)
    second_approach(n, parents)


if __name__ == "__main__":
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10 ** 7)  # max depth of recursion
    threading.stack_size(2 ** 27)  # new thread will get stack of such size
    threading.Thread(target=main).start()
