#!/usr/bin/python3
''' a class Student that defines a student
'''


class Student:
    """base class or super class"""

    def __init__(self, first_name, last_name, age):
        '''method __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public instance method """
        if (type(attrs) == list and
            any(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
