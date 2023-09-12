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
        """Gets student dictionary representation.

        If attrs is a  string list, only represent attributes
        included in the list.

        Args:
            attrs (list): (Optional) Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all student attributes.

        Args:
            json (dict): The attributes to replace key/value pairs with.
        """
        for k, v in json.items():
            setattr(self, k, v)
