#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Restricts user instantiation of new LockedClass attributes
    to only the attribute 'first_name'.
    """

    __slots__ = ["first_name"]
