import math
import sys
from typing import List


def largest_number(nums: List[int]) -> str:
    """
    Naive apporach:
    Unfortunately this only works for single digit numbers.
    """
    largest_combination: List[int] = []
    while nums:
        max_digit = -math.inf
        for n in nums:
            if max_digit < n:
                max_digit = n

        nums.remove(max_digit)
        largest_combination.append(max_digit)

    return "".join(str(n) for n in largest_combination)


def find_largest_number(numbers: List[int]) -> str:
    largest_combination: List[int] = []
    while numbers:
        max_digit = 0
        for n in numbers:
            if is_greater_or_equal(n, max_digit):
                max_digit = n

        numbers.remove(max_digit)
        largest_combination.append(max_digit)

    return "".join(str(n) for n in largest_combination)


def is_greater_or_equal(a: str, b: str):
    return int(f"{a}{b}") >= int(f"{b}{a}")


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    assert n == len(numbers)
    print(find_largest_number(numbers))
