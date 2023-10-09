#!/usr/bin/python3
"""Defines a function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Returns True if the _object is an instance of or if the object is,
    an instance of a class that _inherited from, the specified _class;
    otherwise False.

    Args:
        obj (a_class): object to check type.
        a_class (type): type of type to check.

    Returns:
        _boolean: True or False.
    """
    return isinstance(obj, a_class)
