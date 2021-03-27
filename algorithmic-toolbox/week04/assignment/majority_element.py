from collections import Counter
from typing import List

NOT_FOUND = -1


def another_approach(items):
    """Boyer Moore algorithm
    Time complexity: O(n)
    Space complexity: O(1)
    """
    candidate = None
    count = 0
    for item in items:
        if item == candidate:
            count += 1
        elif item != candidate:
            count -= 1
        elif count == 0:
            candidate = item
    return candidate


def majority_element(array: List[int]):
    """
    Solve majority element problem using divide and conquer method.
    >>> majority_element([2, 3, 9, 2, 2])
    2
    >>> majority_element([1, 2])
    -1
    >>> majority_element([1])
    1
    """
    return recursive_majority_element(array, 0, len(array) - 1)


def recursive_majority_element(array: List[int], i: int, j: int):
    if i == j:
        return array[i]

    mid: int = (i + j) // 2

    left = recursive_majority_element(array, i, mid)
    right = recursive_majority_element(array, mid + 1, j)

    if left == right:
        return left

    left_counts = array.count(left)
    right_counts = array.count(right)

    if left_counts > len(array) // 2:
        return left
    elif right_counts > len(array) // 2:
        return right
    else:
        return NOT_FOUND


if __name__ == "__main__":
    n = int(input())
    array = [int(item) for item in input().split()]

    assert n == len(array)

    c = Counter(array)
    first_most_common = c.most_common(1)[0]
    frequency = first_most_common[1]

    if frequency > len(array) / 2:
        print(1)
    else:
        print(0)
