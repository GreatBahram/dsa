from typing import Any, Sequence


def linear_search(array: Sequence[Any], key: Any) -> bool:
    """
    Time complexity: O(n)
    """
    for item in array:
        if item == key:
            return True
    return False


def binary_search(array: Sequence[Any], key: Any) -> bool:
    """
    It requires us to sort the array before passing it to the 
    binary_search function, and this will cost  O(n log n).
    T(n) = T(n/2) + O(1), according to the Master theorem this costs
    (logn).
    Time complexity: O(log n)
    """
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
