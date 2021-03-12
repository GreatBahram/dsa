import math


def top_down_edit_distance(str1: str, str2: str, m: int, n: int) -> int:
    """
    m: is len(str1)
    n: is len(str2)
    It will take a long time for a large strings.
    example:
    >>> top_down_edit_distance("dinitrophenylhydrazine", "benzalphenylhydrazone", 22, 21)

    """
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return top_down_edit_distance(str1, str2, m - 1, n - 1)
    return 1 + min(
        top_down_edit_distance(str1, str2, m, n - 1),
        top_down_edit_distance(str1, str2, m - 1, n),
        top_down_edit_distance(str1, str2, m - 1, n - 1),
    )


def generate_memo(rows: int, cols: int):
    memo = []
    row = [0] + [math.inf for i in range(cols)]

    memo = [list(row) for i in range(rows + 1)]

    memo[0] = [i for i in range(cols + 1)]
    for i in range(rows + 1):
        memo[i][0] = i

    return memo


def edit_distance(str1: str, str2: str) -> int:
    """
    Return the minimum number of operations (insertions, deletions, and
    substitutions of symbols) to transform one string into another
    """
    memo = generate_memo(len(str2), len(str1))
    str1 = "_" + str1
    str2 = "_" + str2
    for j in range(1, len(str2)):
        for i in range(1, len(str1)):
            if str1[i] == str2[j]:
                memo[j][i] = memo[j - 1][i - 1]
            else:
                memo[j][i] = min(memo[j][i - 1], memo[j - 1][i], memo[j - 1][i - 1]) + 1
    min_ops = memo[-1][-1]
    return min_ops


if __name__ == "__main__":
    print(edit_distance(input(), input()))
