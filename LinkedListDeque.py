from deque import Deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None  # next node, or None if end
        self.prev: Node | None = None  # previous node, or None if start

class LinkedListDeque:
    def __init__(self):
        self.head: Node | None = None  # Points to the front of deque
        self.tail: Node | None = None  # Points to the back of deque

    def is_empty(self) -> bool:
        return self.head is None

    def add_to_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            if self.head is not None:  # Check that head is not None
                self.head.prev = new_node
            self.head = new_node

    def add_to_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            if self.tail is not None:  # Check that tail is not None
                self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if self.is_empty():
            raise IndexError("Cannot remove from front, deque is empty.")
        if self.head is not None:
            value = self.head.value  # Accessing value safely
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
            return value
        raise ValueError("Head is None")

    def remove_from_back(self):
        if self.is_empty():
            raise IndexError("Cannot remove from back, deque is empty.")
        if self.tail is not None:
            value = self.tail.value  # Accessing value safely
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.next = None
            return value
        raise ValueError("Tail is None")

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        if self.head is not None:
            return self.head.value  # Safely accessing head's value
        raise ValueError("Head is None")

    def peek_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        if self.tail is not None:
            return self.tail.value  # Safely accessing tail's value
        raise ValueError("Tail is None")
