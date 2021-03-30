import sys
from typing import List


def naive_partition3(nums: List[int]) -> bool:
    """
    Brute force approach in order to capture the essence
    of this problem.
    """
    target, remaining = divmod(sum(nums), 3)
    if remaining:
        return False

    def sum_subset3(nums: List[int], n: int, a: int, b: int, c: int) -> bool:
        if a == 0 and b == 0 and c == 0:
            return True
        if n < 0:
            return False

        used_in_a = used_in_b = used_in_c = False

        if a - nums[n] >= 0:
            used_in_a = sum_subset3(nums, n - 1, a - nums[n], b, c)

        if not used_in_a and b - nums[n] >= 0:
            used_in_b = sum_subset3(nums, n - 1, a, b - nums[n], c)

        if (not used_in_a and not used_in_b) and c - nums[n] >= 0:
            used_in_c = sum_subset3(nums, n - 1, a, b, c - nums[n])

        return used_in_a or used_in_b or used_in_c

    return sum_subset3(nums, len(nums) - 1, target, target, target)


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
