#!/usr/bin/python3
"""Returns a function lookup()"""


def lookup(obj):
    """_Function that returns the list of available _attributes and _methods,
    for an object

    Args:
        obj (class): object

    Returns:
        list: list of available _attributes and _methods of an _object
    """
    return dir(obj)
