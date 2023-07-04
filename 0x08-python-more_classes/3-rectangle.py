#!/usr/bin/python3

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

    def area(self):
        """returns the area of a rectangle"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (int(self.__width * 2) + int(self.__height * 2))

    def __str__(self):
        """print empty line if zero"""
        if self.width == 0 or self.height == 0:
            return ""
        
        prim = ""
        for _ in range(self.height):
            prim += "#" * self.width
            prim += "\n"
        return str(prim)
