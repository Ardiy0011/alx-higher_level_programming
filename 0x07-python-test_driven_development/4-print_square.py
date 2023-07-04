#!/usr/bin/python3
"""
module that prints out the hashed square shape
"""
def print_square(size):
    """
    Function to print out the hashed square shape

    Args:
        a (size): consituttes length and width of square

    Returns:
        none

    Raises:
        TypeError: If size isnt an integer of if size is a float or less than 0
        ValueError: if size is less than 0
      
    """
    try :
        if not isinstance(size, int) or (isinstance(size, float) and size < 0):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for _ in range(size):
            for _ in range(size):
                print("#",end="")
            print()
    except (TypeError, ValueError)as e:
        print(e)
