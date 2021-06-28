from typing import Any, Union


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.parent: Node = None
        self.height: int = 0

    def __repr__(self) -> str:
        return f"Node(value={self.value}, height={self.height})"


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


def avl_insert(root: Node, key):
    insert(root, key)
    found_node = find(root, key)
    rebalance(found_node)


def rebalance(node: Node):
    parent = node.parent

    if (node.left and node.right) and node.left.height > node.right.height + 1:
        rebalance_right(node)
    if (node.left and node.right) and node.right.height > node.left.height + 1:
        rebalance_left(node)

    adjust_height(node)
    if parent is not None:
        rebalance(parent)


def adjust_height(node: Node) -> None:
    node.height = 1 + max(
        node.left.height if node.left else 0, node.right.height if node.right else 0
    )


def rebalance_right(node: Node):
    m = node.left

    if m.right.height > m.left.height:
        rotate_left(m)
    rotate_right(n)
    adjust_height(m)
    adjust_height(n)


def rebalance_left(node: Node):
    m = node.right

    if m.left.height > m.right.height:
        rotate_right(m)
    rotate_left(n)
    adjust_height(m)
    adjust_height(n)


def rotate_right(node):
    parent = node.parent
    y = node.left
    b = y.right

    y.parent = parent

    # assign y on the proper side of the parent
    if parent is not None:
        if parent.left.value == node.value:
            parent.left = y
        else:
            parent.right = y
    node.parent = y
    y.right = node

    b.parent = node
    node.left = b
    return y


def rotate_left(node):
    parent = node.parent
    x = node.right
    b = x.left

    x.parent = parent

    # assign y on the proper side of the parent
    if parent is not None:
        if parent.left.value == node.value:
            parent.left = x
        else:
            parent.right = x
    node.parent = x
    x.left = node

    b.parent = node
    node.right = b
    return x
