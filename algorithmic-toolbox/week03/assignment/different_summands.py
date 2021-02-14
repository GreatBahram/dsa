import sys
from typing import List


def optimal_summands(n: int) -> List[int]:
    summands: List[int] = []
    increment: int = 1
    remainder: int = n - 1

    if n < 3:
        summands.append(n)
        return summands

    summands.append(1)

    while remainder > 0:
        if remainder <= summands[-1]:
            summands.append(summands.pop() + remainder)
            remainder = 0
        else:
            increment += 1
            summands.append(increment)
            remainder -= increment
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)

    summands = optimal_summands(n)

    print(len(summands))
    for x in summands:
        print(x, end=" ")
