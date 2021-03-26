from typing import Sequence


def selection(numbers: Sequence[int]) -> None:
    """Sort numbers in-place."""
    for i in range(len(numbers)):
        min_index = i

        # find minimum item from numbers[i + 1:]
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
