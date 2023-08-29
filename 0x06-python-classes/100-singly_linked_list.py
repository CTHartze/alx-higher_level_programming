#!/usr/bin/python3
"""Defines classes and nodes for singly-linked list."""

class Node:
    """Singly-linked list node representative."""

    def __init__(self, data, next_node=None):
        """
        New node initializer.

        Args:
            data (int): Refers to new node data.
            next_node (Node): New nodes next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets/sets node data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets/sets next_node of node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly-linked list representative."""

    def __init__(self):
        """New SinglyLinkedList initializer."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new node in SinglyLinkedList.

        Inserts node into list at correct
        ordered numerical position.

        Args:
            value (Node): Refers to new node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines print() representation of SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
