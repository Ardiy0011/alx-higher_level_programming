#!/usr/bin/python3
'''
    Creating the base class of all other classes for this project.
'''
import json
import csv


class Base:
    '''
        This class will manage the id attribute for all the classes.
        Arguments:
            @id: The id for a specific instance.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
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


    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
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
        except:
            return []

        insts = []

        for instance in content:
            tmp = cls.create(**instance)
            insts.append(tmp)

        return (insts)