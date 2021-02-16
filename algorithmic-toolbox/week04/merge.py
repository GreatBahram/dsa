from typing import Sequence


def merge_sort(numbers: Sequence[int]) -> Sequence[int]:
    if len(numbers) < 2:
        return numbers

    m = len(numbers) // 2
    # Split the list into two halves
    left = numbers[:m]
    right = numbers[m:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: Sequence[int], right: Sequence[int]) -> Sequence[int]:
    results = []

    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            results.append(left[left_index])
            left_index += 1
        else:
            results.append(right[right_index])
            right_index += 1

    if left:
        results.extend(left[left_index:])

    if right:
        results.extend(right[right_index:])

    return results
