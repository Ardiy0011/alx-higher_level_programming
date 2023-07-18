#!/usr/bin/python3
"""imports base class to derived class rectangle"""


from models.base import Base


"""Defines a Base class."""


class Rectangle(Base):
    """Represents a derived class fom base"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args/constructors:
            width : The width of the new Rectangle.
            height : The height of the new Rectangle.
            x : The x coordinate of the new Rectangle.
            y : The y coordinate of the new Rectangle.
            id : The identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a rectangle"""
        return int(self.__width) * int(self.__height)

    def display(self):
        """prints hash representatitons"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """calling this str function to override the internal stdout"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}")


    def update(self, *args, **kwargs):
        """assign non keyword argument to attribute via their indexes"""

        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return

        try:
            if len(args) == 0:
                raise IndexError("out of range")
        except IndexError as e:
            print(e)

        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """
        Dictionary representation of the Square.
        """
        dictionary ={'x': self.x,
                    'y': self.y,
                    'id': self.id,
                    'height': self.height,
                    'width': self.width}

        return dictionary
