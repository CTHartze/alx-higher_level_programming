#!/usr/bin/python3
"""Defines class square according to 4-square.py."""

class Square:
    """Square representative."""

    def __init__(self, size):
        """
        Square initializer.

        Args:
            size (int): Refers to size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the squares current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the squares current area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
