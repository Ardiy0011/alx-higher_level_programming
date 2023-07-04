#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """retrieves attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets attribute value"""
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except (TypeError, ValueError) as e:
            print(e)

    @property
    def height(self):
        """retrieves attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets attribute value"""
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            print(e)
