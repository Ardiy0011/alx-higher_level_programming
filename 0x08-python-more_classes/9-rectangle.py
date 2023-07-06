#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """public class field"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """new instance created"""
        return cls(size, size)
    
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

    def __init__(self, width=0, height=0):
        '''method to initialize instance of class Rectangle
        '''
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''gets the width aspect of rectangle

        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''sets the width aspect of rectangle
        '''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: set_height getter
        '''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''method that sets a method
        '''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''method that returns area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''method that returns perimeter of perimeter
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''method that returns nice string representation of rectangle
        '''
        rectrt = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            rectrt += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                rectrt += '\n'
        return rectrt

    def __repr__(self):
        '''method that creates a new object
        '''
        rectrt = "Rectangle(" + str(self.__width) + ","
        rectrt += str(self.__height) + ")"
        return rectrt

    def __del__(self):
        '''method that deletes instance of Rectangle class, and prints "bye" message
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
