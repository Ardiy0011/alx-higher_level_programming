#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """initializing empty rectangle class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets attribute value"""
        try:
            if not isinstance(self.__width, int) or isinstance(self.__width, bool):
                raise TypeError("width must be an integer")
            if self.__width < 0:
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
            if not isinstance(self.__width, int) or isinstance(self.__width, bool):
                raise TypeError("width must be an integer")
            if self.__width < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            print(e)

    def area(self):
        """returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))  

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = ['#' * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

