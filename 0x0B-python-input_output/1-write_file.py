#!/usr/bin/python3
"""
function that writes onto a text file
"""


def write_file(filename="", text=""):
    """
    function that opens and reads a file
    """
    with open(filename, 'w', encoding='UTF-8') as q:
        peruse = q.write(text)

        return (peruse)
