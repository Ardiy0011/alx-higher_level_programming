#!/usr/bin/python3
import json
"""Defines a Base class."""


class Base:
    """Represents a base class with a private instnace variable"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new bass class.
        Args:
            id (int): public isntance variable.
        """
        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string rep of list of dictionaries"""

        if list_dictionaries == None or len(list_dictionaries) == 0:
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
        """Writes the string representation of objects of a class into a file"""
        filename = cls.__name__ + ".json"
        lines = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                lines.append(obj_dict)
        with open(filename, mode="w") as f:
            json.dump(lines, f)
