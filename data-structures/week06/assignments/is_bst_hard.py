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


def is_bst_second(node: Node, left, ceil) -> bool:
    if not node:
        return True
    if node.value >= :
      return False
    
    if ceil and node.value >
    if node.value <= floor or node.value > ceil:
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
