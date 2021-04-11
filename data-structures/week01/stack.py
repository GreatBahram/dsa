from abc import ABCMeta, abstractmethod


class BaseStack(ABCMeta):
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass


class Stack(BaseStack):
    """Implementing a Stack using an array."""

    def __init__(self):
        self._container = []

    def push(self, value):
        self._container.append(value)

    def pop(self):
        if not self.empty:
            self._container.pop()

    @property
    def empty(self):
        return len(self._container) == 0


class StackLL(BaseStack):
    """Stack using Linked List."""
