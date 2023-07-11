#!/usr/bin/python3
"""subclass that inherits from a base class list"""


class BaseGeometry:
    """
    function that prints the sorted list from the base class
    """
    def area(self):

        raise Exception("area() is not implemented")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
