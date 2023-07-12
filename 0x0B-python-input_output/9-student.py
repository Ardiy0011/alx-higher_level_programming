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

    def to_json(self):
        """public instance method dict rep"""
        return self.__dict__
