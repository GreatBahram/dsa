"""
http://www.algorithmsandme.com/runway-reservation-system/

MIT Binary Search Trees
https://www.youtube.com/watch?v=9Jry5-82I68
"""
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None


def inorder(node: Node):
    if not node:
        return None
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def add_node(node: Node, value: int, k: int):
    if not node:
        return Node(value)

    if (node.value - k < value) and (node.value + k > value):
        return node

    if node.value > value:
        node.left = add_node(node.left, value, k)
    else:
        node.right = add_node(node.right, value, k)

    return node


def main():
    root = add_node(None, 30, 3)
    add_node(root, 20, 3)
    add_node(root, 15, 3)
    add_node(root, 25, 3)
    add_node(root, 40, 3)
    add_node(root, 38, 3)
    add_node(root, 45, 3)

    inorder(root)


if __name__ == "__main__":
    main()
