#!/usr/bin/python3
"""
Derived class for BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """derived class of base class BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
