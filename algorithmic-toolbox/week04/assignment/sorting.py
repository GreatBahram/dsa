# Uses python3
import random
import sys
from typing import List, Tuple


def partition3(a: List[int], l: int, r: int) -> Tuple[int, int]:
    i = l
    lt = l
    gt = r
    pivot = a[l]

    while i <= gt:
        if a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        elif a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
            pass
        else:
            i += 1
    return lt, gt


def partition2(a, l, r) -> int:
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    # swap the pivot to its final position
    a[l], a[j] = a[j], a[l]

    return j


def non_recursive_qsort(array: List[int]):
    """
    Easy way, with some additional space!
    """
    if len(array) < 2:
        return array

    less = []
    equal = []
    more = []

    # random pivot index
    k = random.randint(0, len(array) - 1)
    pivot = array[k]
    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            more.append(element)
        else:
            equal.append(element)

    return non_recursive_qsort(less) + equal + non_recursive_qsort(more)


def randomized_quick_sort(a, left: int, right: int) -> None:
    if left >= right:
        return None
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]

    m1, m2 = partition3(a, left, right)
    randomized_quick_sort(a, left, m1 - 1)
    randomized_quick_sort(a, m2 + 1, right)


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *items = list(map(int, input.split()))
    randomized_quick_sort(items, 0, n - 1)
    for x in items:
        print(x, end=" ")
