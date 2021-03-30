import sys
from typing import List


def optimal_weight(weights: List[int], constraint: int) -> int:
    """
    Using top-down approach:
    https://www.youtube.com/watch?v=xOlhR_2QCXY
    """
    row = [0] + [-1 for i in range(constraint)]
    memo = [list(row) for i in range(len(weights))]

    def top_down_knapsack(n, constraint):
        if memo[n][constraint] != -1:
            return memo[n][constraint]

        if n == 0 or constraint == 0:
            result = 0
        elif weights[n] > constraint:
            result = top_down_knapsack(n - 1, constraint)
        else:
            tmp1 = weights[n] + top_down_knapsack(n - 1, constraint - weights[n])
            tmp2 = top_down_knapsack(n - 1, constraint)
            result = max(tmp1, tmp2)
        memo[n][constraint] = result
        return result

    return top_down_knapsack(len(weights) - 1, constraint)


def bt_knapsack(weights: List[int], constraint: int):
    row = [0] * (constraint + 1)
    memo = [list(row) for _ in range(len(weights))]
    for j in range(len(weights)):
        for i in range(constraint + 1):
            if j == 0 or i == 0:
                memo[j][i] = 0
            elif weights[j] <= i:
                memo[j][i] = max(
                    memo[j - 1][i], weights[j] + memo[j - 1][i - weights[j]]
                )
            else:
                memo[j][i] = memo[j - 1][i]

    return memo[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    constraint, n, *weights = list(map(int, input.split()))
    weights = [0] + weights
    print(optimal_weight(weights, constraint))
