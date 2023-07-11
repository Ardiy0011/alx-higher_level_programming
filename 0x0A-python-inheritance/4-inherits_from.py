#!/usr/bin/python3
"""subclass that inherits from a base class list"""


def inherits_from(obj, a_class):
    """
    function that prints the sorted list from the base class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
