#!/usr/bin/python3
"""
module printing strings
"""


def say_my_name(first_name, last_name=""):

    """
    Function to print two strings.

    Args:
        a (first_name): the entire matrix/list of lists
        b (last_name): The divisor.

    Returns:
        stdout strinf literals with embedded formated strings

    Raises:
        TypeError: If first and second names arent strings
        TypeError: If each row of the matrix aren't the same size or length
        TypeError: if name is a character or empty
  
    """
    try:
        if not isinstance (first_name, str):
            raise TypeError ("first_name must be a string")
        if not isinstance (last_name, str):
            raise TypeError ("last_name must be a string")
        if len(first_name) < 2:
            print("Please provide a first name and last name with at \
least 2 characters each")
        else:
            print("My name is {} {}".format(first_name, last_name))
    except TypeError as e:
        print(e)
