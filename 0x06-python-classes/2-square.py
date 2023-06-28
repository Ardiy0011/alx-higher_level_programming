#!/usr/bin/python3

"""Define a class Square."""

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, vva):
        if not isinstance(vva, int):
            raise TypeError("size must be an integer")
        elif vva < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = vva
