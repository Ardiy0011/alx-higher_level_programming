#!/usr/bin/python3
"""class with validators"""


class BaseGeometry:
    """base class of chain of inheritance"""
    def area(self):
        """
        function that prints the sorted list from the base class
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        function that prints the sorted list from the base class

        Raises:
        TypeError: If value not int an name not str
        valueError: if value equal to or less than 0
        TypeError: if empty

        """
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        if not isinstance(name, str):
            raise TypeError("place a string instead of {}".format(self.name))

class Rectangle(BaseGeometry):
    """derived class of base class BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
