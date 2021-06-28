from typing import Any, Union


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.parent: Node = None

    def __repr__(self) -> str:
        return f"Node(value={self.value})"


def find(root: Node, key: Any) -> Union[None, Node]:
    """Search in the tree for a given key."""
    if root is None:
        return None
    if root.value == key:
        return root
    elif root.value > key:
        return find(root.left, key)
    elif root.value < key:
        return find(root.right, key)
    return None


def modified_find(root, key) -> Node:
    """
    Modified find will return the best position of a given node
    if that does not exist in the tree."""
    if root.value == key:
        return root
    elif root.value > key:
        if root.left is not None:
            return modified_find(root.left, key)
        return root
    # elif root.value < key:
    else:
        if root.right is not None:
            return modified_find(root.right, key)
        return root


def next_element(node: Node) -> Node:
    if node.right is not None:
        return left_descendant(node.right)
    return right_ancestor(node)


def left_descendant(node: Node) -> Node:
    while node.left is not None:
        node = node.left
    return node


def right_ancestor(node: Node) -> Node:
    """This function only works when you have parent pointer."""
    if node.parent is None:
        return node
    if node.value < node.parent.value:
        return node.parent
    return right_ancestor(node.parent)


def range_search(root, frm, to) -> list[Node]:
    list_of_nodes = list()
    next_node = modified_find(root, frm)
    while next_node.value <= to:
        if next_node.value >= frm:
            list_of_nodes.append(next_node)
        next_node = next_element(next_node)
    return list_of_nodes


def insert(node: Node, key) -> Node:
    if node is None:
        return Node(key)
    if node.value > key:
        node.left = insert(node.left, key)
        node.left.parent = node
    else:  # if it is less than key
        node.right = insert(node.right, key)
        node.right.parent = node
    return node


def min_value(node: Node):
    while node.left is not None:
        node = node.left
    return node


def delete(root: Node, key):
    if root is None:
        return root

    if root.value > key:
        root.left = delete(root.left, key)
    elif root.value < key:
        root.right = delete(root.right, key)
    else:
        # return the right child as the new root.
        if root.left is None:
            temp = root.right
            root = None
            return temp
        # return the left child as the new root.
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # find the successor node
        temp = min_value(root.right)

        # replace the successor with root node
        root.value = temp.value

        # remove the sucessor from the sub-tree
        delete(root.right, temp.value)
    return root
