import math
from typing import List, Tuple


def find_two_largest(nums: List[int]) -> Tuple[int]:
    if len(nums) <= 2:
        return nums

    first = second = -math.inf

    for number in nums:
        if number >= first:
            second = first
            first = number
        elif number >= second:
            second = number
    return (first, second)


if __name__ == "__main__":
    import operator
    import sys
    from functools import reduce

    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    assert n == len(nums)

    print(reduce(operator.mul, find_two_largest(nums)))
