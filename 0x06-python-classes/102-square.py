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
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """area of  square."""
        return int(self.__size) * int(self.__size)

    def __lt__(self, other):
        """general comparison."""
        if isinstance(other, Square):
            return (
                self.__size < other.__size,
                self.__size <= other.__size,
                self.__size == other.__size,
                self.__size != other.__size,
                self.__size > other.__size,
                self.__size >= other.__size
            )
        return NotImplemented
