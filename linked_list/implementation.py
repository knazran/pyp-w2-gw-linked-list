from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        # Define start node
        self.start = None
        # Define end node
        self.end = None
        self.length = 0
        if (elements is None) or len(elements) == 0:
            return
        else:
            # Link nodes together
            self.length = len(elements)  # An internal counter on our list length
            for elem in elements:
                temp_node = Node(elem)

                if self.start is None:
                    self.start = temp_node
                    self.end = temp_node
                else:
                    self.end.next = temp_node
                    self.end = temp_node

    def __str__(self):
        # Rebuild our array
        current_node = self.start
        array = []

        while current_node:
            array.append(current_node.elem)
            current_node = current_node.next
        return str(array)

    def __len__(self):
        return self.length

    def __iter__(self):
        pass

    def __getitem__(self, index):
        # check for index length
        if index >= self.length:
            raise IndexError
        # We need to iterate the chain
        return_node = self.start
        for idx in range(0, index):
            return_node = return_node.next
        return return_node.elem

    def __add__(self, other):
        # We hacked this via array
        array = []

        # for self
        currentself_node = self.start
        while currentself_node:
            array.append(currentself_node.elem)
            currentself_node = currentself_node.next

        # for other
        currentother_node = other.start
        while currentother_node:
            array.append(currentother_node.elem)
            currentother_node = currentother_node.next
        return LinkedList(array)

    def __iadd__(self, other):
        self = self.__add__(other)
        return self

    def __eq__(self, other):
        # length check
        if self.length == other.length:
            # This is O(n^2) complexity. There is a better way
            for idx in range(0, self.length):
                if self[idx] != other[idx]:
                    return False
            return True
        return False

    def __ne__(self, other):
        # Just call the __eq__ magic method
        return not self.__eq__(other)

    def append(self, elem):
        node_append = Node(elem)

        # If we have existing chain
        if self.length != 0:
            self.end.next = node_append
            self.end = node_append
        else:
            # If we don't have an existing chain
            self.start = node_append
            self.end = node_append

        # Add our internal length counter
        self.length = self.length + 1
        # pass

    def count(self):
        return self.length

    def pop(self, index=None):
        # Handle empty list
        if self.length == 0:
            raise IndexError

        # Pop the last element by default
        if index is None:
            target_index = self.length - 1
        else:
            target_index = index
        if target_index >= self.length:
            raise IndexError

        prev = None
        current = self.start
        pos = 0

        # While there is a next ref, and haven't
        while pos < target_index:
            prev = current
            current = current.next
            pos += 1
        # By the end, the current node will be our target node
        if prev is None:
            self.start = current.next
        else:
            prev.next = current.next
        self.length = self.length - 1
        return current.elem
