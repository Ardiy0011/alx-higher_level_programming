#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """public class field"""
    number_of_instances = 0
    print_symbol = "#"

    """initializing empty rectangle class"""
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
        if self.__width == 0 or self.__height == 0:
            return ""

        prim = ""
        for _ in range(self.__height):
            prim += str(self.print_symbol) * self.__width
            prim += "\n"
        return str(prim)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the bigger area"""
        try:
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            
            if rect_1.area() >= rect_2.area():
                return (rect_1)
            elif rect_2.area() > rect_1.area():
                return (rect_2)
        except TypeError as e:
            print(e)

    @classmethod
    def square(cls, size=0):
        """new instance created"""
        return cls(size, size)
