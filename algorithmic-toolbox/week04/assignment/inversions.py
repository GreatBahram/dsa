import sys
from typing import List


def brute_force(array):
    """
    Time complexity: O(n**2)
    Space complexity: O(1)
    """
    inversions = 0
    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            if array[j] > array[i]:
                inversions += 1
    return inversions


def merge_sort_with_inversion(array: List[int]):
    if len(array) < 2:
        return array, 0

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left, left_inversions = merge_sort_with_inversion(left)
    right, right_inversions = merge_sort_with_inversion(right)

    inversions = left_inversions + right_inversions

    sorted_array, merge_inverions = merge_with_inversion(left, right)
    return sorted_array, inversions + merge_inverions


def merge_with_inversion(left, right):
    left_idx = right_idx = inversions = 0
    mid = len(right) - 1
    results = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            results.append(left[left_idx])
            left_idx += 1
        else:
            results.append(right[right_idx])
            right_idx += 1
            # [4, 5], [3, 2, 1]
            inversions += len(left) - left_idx

    if left:
        results.extend(left[left_idx:])

    if right:
        results.extend(right[right_idx:])

    return results, inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *numbers = list(map(int, input.split()))
    sorted_array, inversions = merge_sort_with_inversion(numbers)
    print(inversions)
