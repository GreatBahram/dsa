weights = [0, 1, 2, 4, 2, 5]
values = [0, 5, 3, 5, 3, 2]


def naive_knapsack(n: int, constraint: int) -> int:
    """
    Naive recurusion solution.
    Time complexity: O(2**n)
    https://www.youtube.com/watch?v=xOlhR_2QCXY
    """
    if n == 0 or constraint == 0:
        result = 0
    elif weights[n] > constraint:
        result = naive_knapsack(n - 1, constraint)
    else:
        tmp1 = values[n] + naive_knapsack(n - 1, constraint - weights[n])
        tmp2 = naive_knapsack(n - 1, constraint)  # no do not select this item
        result = max(tmp1, tmp2)
    return result


def knapsack(n, constraint):
    """
    Top-down approach
    https://www.youtube.com/watch?v=xOlhR_2QCXY
    """
    row = [0] + [-1 for i in range(constraint)]
    memo = [list(row) for j in range(n + 1)]

    def top_down_knapsack(n: int, constraint: int) -> int:
        if memo[n][constraint] != -1:
            return memo[n][constraint]

        if n == 0 or constraint == 0:
            result = 0
        elif weights[n] > constraint:
            result = top_down_knapsack(n - 1, constraint)
        else:
            include = values[n] + top_down_knapsack(n - 1, constraint - weights[n])
            exclude = top_down_knapsack(n - 1, constraint)  # no do not select this item
            result = max(include, exclude)
        memo[n][constraint] = result
        return result

    return top_down_knapsack(n, constraint)
