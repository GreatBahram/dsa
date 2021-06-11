"""
This heap is implemented using zero-based indexing.
parent(i) -> (i - 1) // 2
left_child = 2 * i + 1
right_child = 2 * i + 2
"""

import math
from typing import List, Optional


class MaxHeap:
    def __init__(self, items: Optional[List[int]] = None):
        self._container = []

        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        return f"{type(self).__name__}({self._container!r})"

    def insert(self, value: int) -> None:
        self._container.append(value)
        _siftup(self._container, len(self) - 1)

    def extract_max(self) -> int:
        """
        Grab the maximum value at the root and
        replace with the leftmost leaf.
        """
        if not len(self):
            raise Exception("Heap is empty")

        value = self.max()

        self._container[0] = self._container[-1]
        self._container.pop()

        _siftdown(self._container, 0)

        return value

    def __len__(self):
        return len(self._container)

    def max(self):
        if not len(self):
            raise Exception("Heap is empty")
        return self._container[0]

    def remove(self, idx: int):
        """Remove a specific element using its index."""
        self._container[idx] = math.inf
        _siftup(self._container, idx)
        self.extract_max()


def left_child(idx: int) -> int:
    return 2 * idx + 1


def right_child(idx: int) -> int:
    return 2 * idx + 2


def _siftup(array, idx: int) -> None:
    # if parent item is smaller than array[idx], swap it
    parent_idx = (idx - 1) // 2

    if parent_idx < 0:
        return None

    if array[idx] > array[parent_idx]:
        array[idx], array[parent_idx] = array[parent_idx], array[idx]
        _siftup(array, parent_idx)


def _siftdown(array, idx: int) -> None:
    """
    Find maximum value from left or right child
    swap it and do this again.
    """
    max_idx = idx

    l = left_child(idx)
    if l < len(array) and array[l] > array[max_idx]:
        max_idx = l

    r = right_child(idx)
    if r < len(array) and array[r] > array[max_idx]:
        max_idx = r

    if idx != max_idx:
        array[idx], array[max_idx] = array[max_idx], array[idx]
        _siftdown(array, max_idx)
