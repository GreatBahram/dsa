#!/usr/bin/env python3
"""
https://dev.to/racheladaw/finding-max-in-a-stack-iej
"""
import sys
from typing import List


class StackWithMax:
    def __init__(self):
        self._container: List[int] = []
        self._max_values: List[int] = []

    def push(self, value: int) -> None:
        if not self._max_values:
            self._max_values.append(value)
        else:
            self._max_values.append(max(self.max, value))
        self._container.append(value)

    def pop(self):
        if self:
            self._max_values.pop()
            return self._container.pop()
        raise IndexError("pop item from empty list")

    def __len__(self):
        return len(self._container)

    def __repr__(self):
        return repr(self._container)

    @property
    def max(self):
        if self:
            return self._max_values[-1]
        raise IndexError("stack is empty")


if __name__ == "__main__":
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max)
        else:
            assert 0
