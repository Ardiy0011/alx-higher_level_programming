#!/usr/bin/python3
"""
function that returns JSON rep of  object
"""


import json

def to_json_string(my_obj):
    """a function that returns JSON rep of  object (string):"""
    jasonrep = json.dumps(my_obj)
    return jasonrep
