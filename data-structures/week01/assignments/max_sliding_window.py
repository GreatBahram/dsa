"""
    https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""
from collections import deque
from typing import Sequence


def naive_max_sliding_window(sequence, k):
    """
    Time complexity: O(nk)
    """
    maximums = []
    for i in range(len(sequence) - k + 1):
        maximums.append(max(sequence[i: i + k]))

    return maximums


def max_sliding_window(sequence: Sequence[int], k: int):
    """
    Time complexity: O(n)
    space complexity: O(k)
    """
    # a double ended queue to keep the index of the maximum
    # of each window
    buffer = deque()
    n = len(sequence)

    for i in range(k):
        # before adding new element, drop all smaller elements
        while buffer and sequence[i] >= sequence[buffer[-1]]:
            buffer.pop()
        buffer.append(i)

    for i in range(k, n):
        # yield previous window's maximum element
        yield sequence[buffer[0]]

        # remove elements which are not part of the current window
        while buffer and buffer[0] <= i - k:
            buffer.popleft()

        # before adding new element, drop all smaller elements
        while buffer and sequence[i] >= sequence[buffer[-1]]:
            buffer.pop()
        buffer.append(i)
    # yield last window maximum element
    yield sequence[buffer[0]]


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
