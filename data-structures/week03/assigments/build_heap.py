from typing import List


def selection_sort_swaps(data):
    """Build a heap from data in-place.
    Returns a sequence of swaps performed by the algorithm.
    Time complexity: O(n**2)
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def _siftdown(array, idx: int, swaps):
    """
    MinHeap siftdown which puts swap indexes inside swaps array.
    """
    max_idx = idx

    l = 2 * idx + 1
    if l < len(array) and array[l] < array[max_idx]:
        max_idx = l

    r = 2 * idx + 2
    if r < len(array) and array[r] < array[max_idx]:
        max_idx = r

    if idx != max_idx:
        swaps.append((idx, max_idx))

        array[idx], array[max_idx] = array[max_idx], array[idx]
        _siftdown(array, max_idx, swaps)


def build_heap(array: List[int]):
    size = len(array)
    swaps = []
    for i in range(size // 2, -1, -1):
        _siftdown(array, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
