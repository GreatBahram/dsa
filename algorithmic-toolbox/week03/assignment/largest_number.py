import math
import sys
from typing import List


def find_largest_number(numbers: List[int]) -> int:
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
