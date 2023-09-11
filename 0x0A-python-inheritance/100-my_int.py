#!/usr/bin/python3
"""Defines a class MyInt inherited from int."""


class MyInt(int):
    """Inverts == and != int operators."""

    def __eq__(self, value):
        """== opeartor is overridden by != behavior."""
        return self.real != value

    def __ne__(self, value):
        """!= operator is overridden by == behavior."""
        return self.real == value
