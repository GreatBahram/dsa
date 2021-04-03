import sys
import threading


class Node:
    def __init__(self):
        self.parent = None


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
    count = 0
    while node.parent is not None:
        node = node.parent
        count += 1
    return count


def max_height(nodes):
    heights = []
    for i in range(len(nodes)):
        heights.append(find_max_height(nodes[i]))
    return max(heights)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

    for idx, parent_id in enumerate(items):
        if parent_id == -1:
            nodes[idx].parent = ROOT_NODE
        else:
            nodes[idx].parent = nodes[parent_id]


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
