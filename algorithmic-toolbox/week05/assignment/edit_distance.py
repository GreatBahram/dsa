import math


def recursive_edit_distance(str1: str, str2: str, m: int, n: int) -> int:
    """
    m: is len(str1)
    n: is len(str2)
    It will take a long time for a large strings.
    example:
    >>> recusrive_edit_distance("dinitrophenylhydrazine", "benzalphenylhydrazone", 22, 21)

    """
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return recursive_edit_distance(str1, str2, m - 1, n - 1)
    return 1 + min(
        recursive_edit_distance(str1, str2, m, n - 1),
        recursive_edit_distance(str1, str2, m - 1, n),
        recursive_edit_distance(str1, str2, m - 1, n - 1),
    )


def top_down_edit_distance(str1, str2):
    """
    m: is len(str1)
    n: is len(str2)
    """
    row = [-1 for i in range(len(str1) + 1)]
    memo = [list(row) for i in range(len(str2) + 1)]

    def tp_edit_distance(str1, str2, m: int, n: int):
        if m == 0:
            return n
        if n == 0:
            return m

        if memo[n][m] != -1:
            return memo[n][m]

        if str1[m - 1] == str2[n - 1]:
            if memo[n - 1][m - 1] != -1:
                memo[n][m] = memo[n - 1][m - 1]
                return memo[n][m]
            else:
                memo[n][m] = tp_edit_distance(str1, str2, m - 1, n - 1)
                return memo[n][m]
        else:
            if memo[n - 1][m] != -1:
                value1 = memo[n - 1][m]
            else:
                value1 = tp_edit_distance(str1, str2, m -1, n)

            if memo[n - 1][m - 1] != -1:
                value2 = memo[n - 1][m - 1]
            else:
                value2 = tp_edit_distance(str1, str2, m -1, n - 1)

            if memo[n][m - 1] != -1:
                value3 = memo[n][m - 1]
            else:
                value3 = tp_edit_distance(str1, str2, m, n - 1)
            memo[n][m] = min(value1, value2, value3) + 1
            return memo[n][m]

    return tp_edit_distance(str1, str2, len(str1), len(str2))


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
