from typing import List

NOT_FOUND = -1


def binary_search(sorted_array: List[int], key: int) -> int:
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] < key:
            low = mid + 1
        elif sorted_array[mid] > key:
            high = mid - 1
        else:  # this is it, baby!
            return mid

    return NOT_FOUND


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return NOT_FOUND


if __name__ == "__main__":
    first_line: List[int] = [int(item) for item in input().split()]
    n, sorted_data = first_line[0], first_line[1:]
    second_line: List[int] = [int(item) for item in input().split()]
    k, search_items = second_line[0], second_line[1:]

    assert n == len(sorted_data)
    assert k == len(search_items)

    for x in search_items:
        print(binary_search(sorted_data, x), end=" ")
