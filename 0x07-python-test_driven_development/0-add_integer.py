#!/usr/bin/python3
"""
this is a amodule comtaining a sum function
"""


def add_integer(a, b=98):

    """
    Function to add two integers.

    Args:
        a (int): The 1st integer.
        b (int): The 2nd integer.

    Returns:
        int: The sum of the two integers or floats as integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or a float
        TypeError: If both `a` and `b` are integers but `b` is 0.
        TypeError: If only one argument is provided`TypeError`raised.
                   
    """
    try:
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        elif b == 0:
            raise TypeError("yo Two arguments are required, but \
only one provided")

        return int(a + b)

    except TypeError as e:
        return str(e)
