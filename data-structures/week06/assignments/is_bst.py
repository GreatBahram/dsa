import math
import sys
import threading

# max depth of recursion
sys.setrecursionlimit(10 ** 8)
# new thread will get stack of such size
threading.stack_size(2 ** 27)


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
    return nodes[0] if nodes else None


def inorder(node, result: list):
    if not node:
        return None
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)
    return result


def is_bst(node) -> bool:
    """
    Return True if a given tree is Binary search Tree, otherwise False.
    Approach 1: using inorder traversal
    """
    # empty tree is a BST.
    if not node:
        return True
    inorder_traverse = inorder(node, [])
    if any(x > y for x, y in zip(inorder_traverse, inorder_traverse[1:])):
        return False
    return True


def is_bst_second(node: Node, floor, ceil) -> bool:
    """
    Second approach, in this implementation we check that each subtree does
    not violate the Binary search tree by passing the the minimum and
    maximum value that they can have.
    """
    if not node:
        return True
    if node.value < floor or node.value > ceil:
        return False
    left_ok = is_bst_second(node.left, floor, node.value)
    right_ok = is_bst_second(node.right, node.value, ceil)
    return left_ok and right_ok


def main():
    list_of_vertices_info = read_inputs()
    root = create_tree(list_of_vertices_info)
    if is_bst_second(root, floor=-math.inf, ceil=math.inf):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    threading.Thread(target=main).start()
