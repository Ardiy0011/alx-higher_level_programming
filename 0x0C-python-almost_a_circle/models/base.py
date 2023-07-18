#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string rep of list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):

        """Returns a dict from a string"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def save_to_file(cls, list_objs):
        """Writes string repr of objects of a class into a file"""
        filename = cls.__name__ + ".json"
        lines = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                lines.append(obj_dict)
        with open(filename, mode="w") as f:
            json.dump(lines, f)


    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except IOError:
            return []

        insts = []

        for instance in content:
            tmp = cls.create(**instance)
            insts.append(tmp)

        return (insts)
