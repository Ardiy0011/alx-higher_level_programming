#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """function that writes a json formatted string on to a text file"""
    try:
        with open(filename) as q:
            jasonrep = json.load(q)
    except json.decoder.JSONDecodeError:
        return []

    return jasonrep
