#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialization Square.

        Args:
            size (int): The size of the new square.
        """
        if size != float(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """py getter"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """py setter"""
        if value != float(value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """area of  square."""
        return int(self.__size) * int(self.__size)
    
    def my_print(self):
        """print empty line if zero"""
        if self.size == 0:
            print()
        for _ in range(self.size):
            """printing hash square based on obj size"""
            print("#" * self.size )
