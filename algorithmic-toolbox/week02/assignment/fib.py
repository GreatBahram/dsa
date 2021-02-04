from functools import lru_cache


@lru_cache(maxsize=None)
def mfib(n):
    """
    Expedite the recursive Fibonacci algorithm using memoization technique.
    """
    if n < 2:  # base case
        return n
    return mfib(n - 2) + mfib(n - 1)  # recursive case


if __name__ == "__main__":
    n = int(input())
    print(mfib(n))
