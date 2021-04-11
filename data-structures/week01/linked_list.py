"""
https://realpython.com/linked-lists-python/
"""
from typing import Any, List, Optional
from dataclasses import dataclass


@dataclass
class Node:
    data: Any
    next: "Node" = None

    def __str__(self):
        return self.data


class LinkedList:
    """Singly LinkedList without tail pointer."""

    def __init__(self, nodes: Optional[List[Any]] = None):
        self.head: Node = None
        if nodes is not None:
            node = Node(nodes[0])
            self.head = node
            for element in nodes[1:]:
                node.next = Node(element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: None):
        if not isinstance(node, Node):
            raise ValueError(f"expect Node object, got {type(node)}")
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if not isinstance(node, Node):
            raise ValueError(f"expect Node object, got {type(node)}")
        if self.head is None:
            self.head = node
            return None
        for current_node in self:
            pass
        current_node.next = node

    def remove_node(self, target_node_data: Any):
        if self.head is None:
            raise Exception("Linked List is empty")
        if self.head.data == target_node_data:
            self.head = None
            return None
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return None
            else:
                previous_node = node
        raise ValueError(f"Node with data {target_node_data} not found")
