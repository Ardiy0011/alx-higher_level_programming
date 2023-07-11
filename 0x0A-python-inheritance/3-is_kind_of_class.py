#!/usr/bin/python3
"""
subclass that inherits from a base class list
"""


def is_kind_of_class(obj, a_class):
    """
    function that prints the sorted list from the base class
    """
    if isinstance(obj, a_class):
        return True
    return False