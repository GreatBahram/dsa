from typing import Dict


def rfib(n: int) -> int:
    """
    Recursive Fibonacci.
    This implementation takes a very long time to
    compute the Fibonacci number of 50.
    Time complexity: O(2**n)
    """
    if n < 2:  # base case
        return n
    return rfib(n - 2) + rfib(n - 1)  # recursive case


memo: Dict[int, int] = {0: 0, 1: 1}


def dfib(n):
    """
    Expedite the recursive Fibonacci algorithm using memoization technique.
    d stands for using a dictionary as it memoization strucuture.
    """
    if n not in memo:
        memo[n] = dfib(n - 1) + dfib(n - 2)
    return memo[n]


# Simplified dfib function using python's automatic memoization object.
from functools import lru_cache


@lru_cache(maxsize=None)
def mfib(n):
    """
    Expedite the recursive Fibonacci algorithm using memoization technique.
    """
    if n < 2:  # base case
        return n
    return mfib(n - 2) + mfib(n - 1)  # recursive case
