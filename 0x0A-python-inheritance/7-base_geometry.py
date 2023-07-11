#!/usr/bin/python3
"""class with validators"""


class BaseGeometry:

    def area(self):
        """
        function that prints the sorted list from the base class
        """
        raise Exception("area() is not implemented")

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
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        if not isinstance(name, str):
            raise TypeError("place a string instead of {}".format(self.name))

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator(4, 7)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
