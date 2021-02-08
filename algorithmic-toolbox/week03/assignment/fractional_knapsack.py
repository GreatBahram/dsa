import sys
from functools import total_ordering
from typing import List, Tuple


@total_ordering
class Item:
    def __init__(self, weight: int, value: int) -> None:
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other) -> bool:
        return self.cost < other.cost

    def __eq__(self, other) -> bool:
        return self.cost == other.cost


def get_optimal_value(capacity: int, items: List[Item]) -> float:
    total_value = 0.0

    for item in items:
        if capacity == 0:
            return total_value

        amount = min(item.weight, capacity)
        total_value += amount * item.cost
        capacity -= amount

    return total_value


if __name__ == "__main__":
    n, capacity = map(int, sys.stdin.readline().split())
    items = []
    for _ in range(n):
        value, weight = map(int, sys.stdin.readline().split())
        items.append(Item(weight, value))

    sorted_items = sorted(items, reverse=True)

    opt_value = get_optimal_value(capacity, sorted_items)
    print(f"{opt_value:.10f}")
