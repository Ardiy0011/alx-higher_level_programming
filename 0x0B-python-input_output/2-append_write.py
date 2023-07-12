#!/usr/bin/python3
"""
function that appends to a text file
"""


def append_write(filename="", text=""):
    """
    function that Appends a string to the end of a UTF8 text file.
    """
    with open(filename, 'a', encoding='UTF-8') as q:
        peruse = q.write(text)

        return (peruse)
