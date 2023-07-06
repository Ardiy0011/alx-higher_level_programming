#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialization Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
    @property
    def size(self):
        """py getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """py setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of  square."""
        return int(self.__size) * int(self.__size)

    for _ in range(width):
        for _ in range(height):
            print("#")
