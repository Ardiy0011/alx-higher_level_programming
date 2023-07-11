#!/usr/bin/python3
"""class with validators"""


BaseGeometry = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """derived class of base class BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return(self.__width) * (self.__height)


    def __str__(self):
        """ print """
        return ("[{}] {}/{}".format(__class__.__name__, self.__width, self.__height))
