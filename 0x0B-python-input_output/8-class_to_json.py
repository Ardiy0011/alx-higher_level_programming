#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    '''
       returns builds a dictionary
    '''
    return obj.__dict__
