#!/usr/bin/python3


def read_file(filename="my_file_0.txt"):
    """
    function that opens and reads a file
    """
    with open('my_file_0.txt', 'r', encoding='UTF-8') as q:
        Peruse = q.read()
        print(Peruse)
