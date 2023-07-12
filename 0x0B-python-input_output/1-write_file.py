#!/usr/bin/python3

def write_file(filename="my_first_file.txt", text=""):
    """
    function that opens and reads a file
    """
    with open('my_first_file.txt', 'w', encoding='UTF-8') as q:
        peruse = q.write(text)

        return (peruse)

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
