#!/usr/bin/python3
"""imports base class to derived class rectangle"""


from models.rectangle import Rectangle
"""Defines a Base class."""


class Square(Rectangle):
    """Represents a derived class fom Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling constructor attributes with super method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """asigning the value to width to size"""
        return self.width

    @size.setter
    def size(self,value):
        """module Square size setter """
        self.external_validator(value)

        self.width = value

    def __str__(self):
        """inheriting and modifying the rectangle str function
        to override the internal stdout"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.size}")

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
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """
        Dictionary representation of the Square.
        """
        dictionary ={'id': self.id,
                    'x': self.x,
                    'size': self.size,
                    'y': self.y}

        return dictionary


