import sys
from typing import List, Tuple


def get_optimal_value(capacity: int, values_weights: List[Tuple[int, int]]) -> float:
    total_value = 0.0

    for value, weight in values_weights:
        if capacity == 0:
            return total_value

        amount = min(weight, capacity)
        unit_worth = value / weight
        total_value += amount * unit_worth
        capacity -= amount

    return total_value


if __name__ == "__main__":
    # get data
    n, capacity = map(int, sys.stdin.readline().split())
    values_weights = []
    for _ in range(n):
        value, weight = map(int, sys.stdin.readline().split())
        values_weights.append((value, weight))

    # sort the input data by descending order
    sorted_values_weights = sorted(
        values_weights, key=lambda d: d[0] / d[1], reverse=True
    )

    opt_value = get_optimal_value(capacity, sorted_values_weights)
    print(f"{opt_value:.10f}")
