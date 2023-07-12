#!/usr/bin/python3

def write_file(filename="my_first_file.txt", text=""):
    """
    function that opens and reads a file
    """
    with open(filename, 'w', encoding='UTF-8') as q:
        peruse = q.write(text)

        return (peruse)

