#!/usr/bin/python3


def append_write(filename="file_append.txt", text=""):
    """
    function that Appends a string to the end of a UTF8 text file.
    """
    with open('file_append.txt', 'a', encoding='UTF-8') as q:
        peruse = q.write(text)

        return (peruse)

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
