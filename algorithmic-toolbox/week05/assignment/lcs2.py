"""Longest common subsequence of two sequences.
If you want to understand the way I solved this problem,
watch this video on Youtube:
https://www.youtube.com/watch?v=NnD96abizww
"""

import math
import sys


def generate_memo(cols: int, rows: int):
    memo = []
    row = [0] + [math.inf for _ in range(cols)]
    memo = [list(row) for i in range(rows + 1)]
    # specific problem changes
    # Reason: because there is zero subsequence between null string and other strings.
    memo[0] = [0 for item in memo[0]]
    return memo


def lcs2(a: str, b: str):
    memo = generate_memo(len(a), len(b))
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
