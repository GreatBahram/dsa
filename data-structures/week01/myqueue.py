from abc import ABC, abstractmethod
from typing import Any


class BaseQueue(ABC):
    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class EMPTY:
    def __repr__(self):
        return "EMPTY "


class Queue(BaseQueue):
    """
    Queue can be implemented using an array or a linked-list.

    In linked-list:
        Enqueue: LinkedList.push_back
        Dequeue: LinkedList.pop_front

    Array Implementation:
    fixed-sized queue using two pointers and an array.
    Head will always points to the oldest element, while tail
    refers to the point that new item is going to be added.
    """

    def __init__(self, size: int):
        self.size = size
        self.head = self.tail = 0
        self._container = [EMPTY()] * size

    def __repr__(self):
        return repr(self._container)

    @property
    def is_empty(self) -> bool:
        return self.head == self.tail

    @property
    def is_full(self) -> bool:
        return self.head == (self.tail + 1) % self.size

    def enqueue(self, value) -> Any:
        if self.is_full:
            raise RuntimeError("Queue is full")
        self._container[self.tail] = value
        self.tail = (self.tail + 1) % self.size

    def dequeue(self) -> Any:
        if self.is_empty:
            raise RuntimeError("Queue is empty")
        value = self._container[self.head]
        self._container[self.head] = EMPTY()
        self.head = (self.head + 1) % self.size
        return value
