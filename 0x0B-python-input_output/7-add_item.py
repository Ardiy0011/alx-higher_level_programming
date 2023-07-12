#!/usr/bin/python3
import json
import sys

def save_to_json_file(my_obj, filename):
    """function that writes a json formatted string on to a text file"""
    jasonrep = json.dumps(my_obj)

    with open(filename, 'w') as q:
        peruse = q.write(jasonrep)

    return (peruse)


def load_from_json_file(filename):
    """function that writes a json formatted string on to a text file"""
    try:
        with open(filename) as q:
            jasonrep = json.load(q)
    except json.decoder.JSONDecodeError:
        return []

    return jasonrep

try:
    if len(sys.argv) == 1:
        raise Exception

except Exception as e:
    print([])
else:
    item = load_from_json_file('add_item.json')
    item.extend(sys.argv[1:])
    save_to_json_file(item, 'add_item.json')
