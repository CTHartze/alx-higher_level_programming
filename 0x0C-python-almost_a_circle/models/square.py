#!/usr/bin/python3
"""Defines square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square represnetation."""

    def __init__(self, size, x=0, y=0, id=None):
        """New Square initialization.

        Args:
            size (int): The new Square's size.
            x (int): The new Square's x coordinate.
            y (int): The new Square's y coordinate.
            id (int): The new Square's identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Sets/Gets the Squares's size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates Square.

        Args:
            *args (ints): Refers to new attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value attribute pairs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns Square's dictionary representation."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns Square's print() and str() representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
