#!/usr/bin/python3
"""class with validators"""


class BaseGeometry:

    def integer_validator(self, name, value):
        """
        function that prints the sorted list from the base class

        Raises:
        TypeError: If value not int an name not str
        valueError: if value equal to or less than 0
        TypeError: if empty
  

        """
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        if not isinstance(name, str):
            raise TypeError("place a string instead of {}".format(self.name))

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


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        """implementing the area through inheritance"""
        super().__init__(self.__size , self.__size)


    def __str__(self):
        """ print """
        return ("[{}] {}/{}".format(__class__.__name__, self.__size, self.__size))
