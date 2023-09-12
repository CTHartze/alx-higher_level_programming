#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Betokens a student."""

    def __init__(self, first_name, last_name, age):
        """New Student initializer.

        Args:
            first_name (str): Students first name.
            last_name (str): Last name of the student.
            age (int): Refers to the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets students dictionary representation.

        If attrs is a string list, only represents attributes
        included in the list.

        Args:
            attrs (list): (Optional) Represents attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
