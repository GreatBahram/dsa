import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = self.right = None


def read_inputs():
    n = int(input())
    return [tuple(map(int, input().split())) for i in range(n)]


def create_tree(list_of_vertices) -> Node:
    nodes = [Node(value) for value, *_ in list_of_vertices]
    # shape the tree structure
    for idx, (_, left_idx, right_idx) in enumerate(list_of_vertices):
        node = nodes[idx]
        node.left = nodes[left_idx] if left_idx >= 0 else None
        node.right = nodes[right_idx] if right_idx >= 0 else None
    return nodes[0]


def inorder(node: Node):
    if not node:
        return None
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def preorder(node: Node):
    if not node:
        return None
    print(node.value)
    preorder(node.left)
    preorder(node.right)


def postorder(node: Node):
    if not node:
        return None

    postorder(node.left)
    postorder(node.right)
    print(node.value)


def main():
    from contextlib import redirect_stdout
    from io import StringIO

    list_of_vertices_info = read_inputs()
    root = create_tree(list_of_vertices_info)

    fp = StringIO()
    with redirect_stdout(fp):
        inorder(root)
    print(fp.getvalue().strip().replace("\n", " "))

    fp = StringIO()
    with redirect_stdout(fp):
        preorder(root)
    print(fp.getvalue().strip().replace("\n", " "))

    fp = StringIO()
    with redirect_stdout(fp):
        postorder(root)
    print(fp.getvalue().strip().replace("\n", " "))


if __name__ == "__main__":
    threading.Thread(target=main).start()
