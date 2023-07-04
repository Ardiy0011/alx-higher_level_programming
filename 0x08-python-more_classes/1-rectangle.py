#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """initializing empty rectangle class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except (TypeError, ValueError)as e:
            print(e)
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def height(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
        except (TypeError, ValueError)as e:
            print(e)
