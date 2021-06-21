#!/usr/bin/env python3
class Vertex:
    """Vertex of a splay tree"""

    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent


def update(v: Vertex) -> None:
    """
    Update operation which apparently update the vertex sum
    attribute and update the parent of left and right vertices.
    """
    if v is None:
        return None
    v.sum = (
        v.key
        + (v.left.sum if v.left != None else 0)
        + (v.right.sum if v.right != None else 0)
    )
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v) -> None:
    parent = v.parent
    if parent is None:
        return None
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v) -> None:
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


def splay(v):
    """
    Splay operation which means make a given vertex the new root.
    """
    if v is None:
        return None
    while v.parent != None:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    # Implement erase yourself
    pass


def search(x):
    global root
    # Implement find yourself

    return False


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum

    return ans


MODULO = 1_000_000_001

n = int(input())

last_sum_result = 0

for i in range(n):
    line = input().split()
    if line[0] == "+":
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == "-":
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == "?":
        x = int(line[1])
        print("Found" if search((x + last_sum_result) % MODULO) else "Not found")
    elif line[0] == "s":
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
