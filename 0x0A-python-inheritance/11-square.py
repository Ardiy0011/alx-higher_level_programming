#!/usr/bin/python3
"""class with validators"""


BaseGeometry = __import__('10-square').Square


"""
the Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        super().__init__(self.__size, self.__size)


    def __str__(self):
        """ print """
        return ("[{}] {}/{}".format(__class__.__name__, self.__size, self.__size))
