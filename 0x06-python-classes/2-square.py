#!/usr/bin/python3

"""Define a class Square."""
class Square:

    def __init__(self, size=0):
        try:
            self.__size = size
        except TypeError:
            print("Size must be an integer")

        if self.__size < 0:
            raise ValueError("Size must be >= 0")
