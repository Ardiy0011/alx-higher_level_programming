#!/usr/bin/python3
"""
function that saves json to text file
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes a json formatted string on to a text file"""
    jasonrep = json.dumps(my_obj)

    with open(filename, 'a') as q:
        peruse = q.write(jasonrep)

    return (peruse)
