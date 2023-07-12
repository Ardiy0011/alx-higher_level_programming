#!/usr/bin/python3
import json

def from_json_string(my_str):
    """function that reverts a jason strings to python object """
    re_engieer = json.loads(my_str)
    return re_engieer
