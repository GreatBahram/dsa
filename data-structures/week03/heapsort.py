from typing import List

from max_heap import MaxHeap, _siftdown


def naive_heapsort(array: List[int]):
    """
    Time complexity: O(n log n)
    space complexity: O(n) because of the additional space.
    """
    m = MaxHeap()
    for item in array:
        m.insert(item)
    return [m.extract_max() for _ in range(len(array))]


def _modified_siftdown(array, n: int, idx: int):
    """
    Modify the previous _siftdown to accept a size (n).
    """
    max_idx = idx

    l = 2 * idx + 1
    if l < n and array[l] > array[max_idx]:
        max_idx = l

    r = 2 * idx + 2
    if r < n and array[r] > array[max_idx]:
        max_idx = r

    if idx != max_idx:
        array[idx], array[max_idx] = array[max_idx], array[idx]
        _modified_siftdown(array, n, max_idx)


def build_heap(array: List[int]):
    size = len(array)
    for i in range(size // 2, -1, -1):
        _siftdown(array, i)


def heap_sort(array: List[int]):
    build_heap(array)

    n = len(array)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        _modified_siftdown(array, i, 0)


def extract_max(array) -> int:
    if not len(array):
        raise Exception("Heap is empty")

    value = array[0]

    array[0] = array[-1]
    array.pop()

    _siftdown(array, 0)

    return value


def partial_sorting(array, k):
    """K largest algorithm."""
    build_heap(array)
    output = []
    for i in range(k):
        output.append(extract_max(array))
    return output
