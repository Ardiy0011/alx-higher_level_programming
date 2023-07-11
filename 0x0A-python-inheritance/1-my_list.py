#!/usr/bin/python3
"""subclass that inherits from a base class list"""


def print_sorted(self):
    """
    function that prints the sorted list from the base class
    """
    try:
        for item in self:
            if not isinstance(item, int):
                raise TypeError("List items must be an integer")

        print(sorted(self))
    except TypeError as e:
        print(e)
