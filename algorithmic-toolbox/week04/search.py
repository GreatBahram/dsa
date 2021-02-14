from typing import Any, Sequence


def binary_search(array: Sequence[Any], key: Any) -> bool:
    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if array[mid] < key:
            low = mid + 1
        elif array[mid] > key:
            high = mid - 1
        else:
            return True
    return False
