#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """
    function that opens and reads a file
    """
    with open(filename, 'r', encoding='UTF-8') as q:
        Peruse = q.read()
        print(Peruse, end="")
