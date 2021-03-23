from typing import List


def partition(array: List[int], n: int):
    """
    Naive approach to solve partition2 problem.
    """
    total = sum(array)
    if total % 2 != 0:  # because we only have positive integers.
        return False
    # return is_subset(array, n, total // 2)
    return is_subset_dp(array, n, total // 2)


def is_subset(array: List[int], n: int, total: int):
    """
    Time complexity: O(2**n)
    Space complexity: O(1)
    n = len(array)
    """
    if total == 0:
        return True
    if n == 0 and total != 0:
        return False

    if array[n - 1] > total:
        return is_subset(array, n - 1, total)

    exclude = is_subset(array, n - 1, total)
    include = is_subset(array, n - 1, total - array[n - 1])
    return exclude or include


def is_subset_dp(array, n, total) -> bool:
    memo = {}

    def is_subset(array, n, total) -> bool:
        nonlocal memo

        if total == 0:
            return True

        if n == 0 and total != 0:
            return False

        key = (n, total)

        if key not in memo:
            include = is_subset(array, n - 1, total - array[n - 1])
            exclude = is_subset(array, n - 1, total)
            memo[key] = include or exclude

        return memo[key]

    return is_subset(array, len(array), total)
