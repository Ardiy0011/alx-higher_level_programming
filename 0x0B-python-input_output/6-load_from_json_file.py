#!/usr/bin/python3
"""
function that loads a jason formated text file
"""
import json


def load_from_json_file(filename):
    """function that writes a json formatted string on to a text file"""
    try:
        with open(filename) as q:
            jasonrep = json.load(q)
    except json.decoder.JSONDecodeError:
        return []

    return jasonrep
