"""
Find the maximum product of two distinct num-
bers in a sequence of non-negative integers.
"""
import math
from typing import List, Tuple


def naive_algorithm(nums: List[int]) -> int:
    """
    Time complexity: O(n**2)
    """
    max_product = -math.inf

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if max_product < nums[i] * nums[j]:
                max_product = nums[i] * nums[j]
    return max_product


def second_approach(nums: List[int]) -> int:
    """
    Sorted numbers in O(nlogn) and pick two largest items
    """
    max2, max1 = sorted(nums)[-2:]
    return max2 * max1


def best_approach(nums: List[int]) -> Tuple[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if len(nums) <= 2:
        return nums

    first = second = -math.inf

    for number in nums:
        if number >= first:
            second = first
            first = number
        elif number >= second:
            second = number
    return first * second


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    assert n == len(nums)

    print(best_approach(nums))
