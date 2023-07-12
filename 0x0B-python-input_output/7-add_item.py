#!/usr/bin/python3
"""
function that odes both load and saving json files
"""
import json
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

try:
    if len(sys.argv) == 1:
        raise FileNotFoundError
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
