import sys
from typing import List


def partition3(array: List[int]) -> bool:
    """Backtrack solution."""
    target, remaining = divmod(sum(array), 3)
    if remaining:
        return False
    # boolean array for keeping which numbers have been used
    used = [False for i in range(len(array))]
    in_progess = 0
    return is_achieavable(array, 0, used, in_progess, target, subsets=3)


def is_achieavable(
    array: List[int],
    idx: int,
    used: List[bool],
    in_progess: int,
    target: int,
    subsets: int,
):
    if subsets == 1:
        return True
    if in_progess == target:
        return is_achieavable(array, 0, used, 0, target, subsets - 1)

    for i in range(idx, len(array)):
        if not used[i]:
            used[i] = True
            if is_achieavable(
                array, i + 1, used, in_progess + array[i], target, subsets
            ):
                return True
            else:
                used[i] = False
    return False


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *numbers = list(map(int, input.split()))
    print(int(partition3(numbers)))
