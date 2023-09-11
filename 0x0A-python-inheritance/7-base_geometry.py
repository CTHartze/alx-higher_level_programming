#!/usr/bin/python3
"""Defines base geometry class, BaseGeometry."""


class BaseGeometry:
    """Betokens base geometry."""

    def area(self):
        """Aborts implementation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates parameter as integer.

        Args:
            name (str): Refers to parameter name.
            value (int): Refers to parameter to validate.
        Raises:
            TypeError: If value isnt an integer.
            ValueError: If value is smaller than and = 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
