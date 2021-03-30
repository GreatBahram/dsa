"""
Read this first:
    https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

This problem, in fact convers multiple topics, including:
    * Partition problem which is available at partition2, partition k
    more generally. The idea is to find 2 subset which sum of them
    is equal, or more generally k subsets which satisfy the condition.
    https://www.techiedelight.com/partition-problem/
    https://www.youtube.com/watch?v=7BynUy5ml0I
    https://www.geeksforgeeks.org/partition-problem-dp-18/

    There there is sum subset which is part of the above problem as well,
    which you have a set of numbers and an integer m for example and you're
    looking for n numbers which sum of them equals to m.
    https://www.techiedelight.com/subset-sum-problem/
"""
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
    """
    Top-down approach
    https://www.techiedelight.com/subset-sum-problem/
    """
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


def bt_is_subset_dp(array, total) -> bool:
    """
    Bottom-up approach:
    https://www.techiedelight.com/subset-sum-problem/
    """
    # First True is for the column 0
    row = [True] + [False for _ in range(total)]
    memo = [list(row) for _ in range(len(array) + 1)]

    n = len(array)

    for j in range(1, n + 1):
        for i in range(1, total + 1):
            # If we cannot use this element, then the answer
            # is the same as previous one.
            if array[j - 1] > i:
                memo[j][i] = memo[j - 1][i]
            else:
                memo[j][i] = memo[j - 1][i] or memo[j - 1][i - array[j - 1]]

    return memo[n][total]
