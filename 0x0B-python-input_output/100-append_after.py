#!/usr/bin/python3
"""
function that readslines and writes to the next line  a anew string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that appends a new string unto a line after reading the
    peruse in a UTF-8 text file.
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        peruse = file.readlines()

    search_string = False

    with open(filename, 'w', encoding='UTF-8') as file:
        for line in peruse:
            file.write(line)
            if '\n' in line and not search_string:
                file.write(new_string)
