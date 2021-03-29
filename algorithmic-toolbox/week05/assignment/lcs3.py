"""
This might! help you:
    https://www.geeksforgeeks.org/lcs-longest-common-subsequence-three-strings/
Though, I believe all the resources for lcs2 are suffice for this problem as well.
"""
import math
import sys


def naive_recursive_lcs3(str1: str, str2: str, str3, m: int, n: int, o: int) -> int:
    """
    m: is len(str1)
    n: is len(str2)
    o: len(str3)
    """
    if m == 0 or n == 0 or o == 0:
        return 0

    if str1[m - 1] == str2[n - 1] == str3[o - 1]:
        return naive_recursive_lcs3(str1, str2, str3, m - 1, n - 1, o - 1) + 1
    return max(
        naive_recursive_lcs3(str1, str2, str3, m - 1, n, o),
        naive_recursive_lcs3(str1, str2, str3, m, n - 1, o),
        naive_recursive_lcs3(str1, str2, str3, m, n, o - 1),
    )


def lcs3(str1, str2, str3):
    """Bottom-up solution"""
    # create a zeros 3d array
    memo = [
        [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
        for _ in range(len(str3) + 1)
    ]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            for k in range(1, len(str3) + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    memo[k][j][i] = memo[k - 1][j - 1][i - 1] + 1
                else:
                    memo[k][j][i] = max(
                        memo[k - 1][j][i], memo[k][j - 1][i], memo[k][j][i - 1]
                    )
    return memo[-1][-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
