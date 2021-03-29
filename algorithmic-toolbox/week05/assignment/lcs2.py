"""Longest common subsequence of two sequences.
If you want to understand the way I solved this problem,
watch this video on Youtube:
https://www.youtube.com/watch?v=NnD96abizww
"""

import math
import sys


def naive_recursive_lcs2(str1: str, str2: str, m: int, n: int) -> int:
    """
    m: is len(str1)
    n: is len(str2)
    """
    if m == 0:
        return 0
    if n == 0:
        return 0

    if str1[m - 1] == str2[n - 1]:
        return naive_recursive_lcs2(str1, str2, m - 1, n - 1) + 1
    return max(
        naive_recursive_lcs2(str1, str2, m - 1, n),
        naive_recursive_lcs2(str1, str2, m, n - 1),
    )


def tp_lcs2(str1: str, str2: str) -> int:
    """
    Top-down longest common subsequence
    """
    row = [-1 for _ in range(len(str1) + 1)]
    memo = [list(row) for _ in range(len(str2) + 1)]

    def recursive_lcs2(str1: str, str2: str, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        if memo[n][m] != -1:
            return memo[n][m]

        if str1[m - 1] == str2[n - 1]:
            if memo[n - 1][m - 1] != -1:
                memo[n][m] = memo[n - 1][m - 1] + 1
            else:
                memo[n][m] = recursive_lcs2(str1, str2, m - 1, n - 1) + 1
            return memo[n][m]
        else:
            if memo[n - 1][m] != -1:
                value1 = memo[n - 1][m]
            else:
                value1 = recursive_lcs2(str1, str2, m, n - 1)

            if memo[n][m - 1] != -1:
                value2 = memo[n][m - 1]
            else:
                value2 = recursive_lcs2(str1, str2, m - 1, n)

            return max(value1, value2)

    return recursive_lcs2(str1, str2, len(str1), len(str2))


def generate_memo(cols: int, rows: int):
    memo = []
    row = [0] + [math.inf for _ in range(cols)]
    memo = [list(row) for i in range(rows + 1)]
    # specific problem changes
    # Reason: because there is zero subsequence between null string and other strings.
    memo[0] = [0 for item in memo[0]]
    return memo


def lcs2(a: List[str], b: List[str]):
    """Bottom-up longest common subsequence of two sequences."""
    memo = generate_memo(len(a), len(b))
    # NOTE: I added the None prefix to make the calculation easy,
    # for instance a[i] == b[j].
    a = [None] + a
    b = [None] + b

    for j in range(1, len(b)):
        for i in range(1, len(a)):
            if a[i] == b[j]:
                memo[j][i] = 1 + memo[j - 1][i - 1]
            else:
                memo[j][i] = max(memo[j - 1][i], memo[j][i - 1])
    return memo[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
