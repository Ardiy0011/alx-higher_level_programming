#!/usr/bin/python3
"""subclass that inherits from a base class list"""


def is_same_class(obj, a_class):
    """
    function that prints the sorted list from the base class
    """
    if isinstance(type(obj), a_class):
        return True
