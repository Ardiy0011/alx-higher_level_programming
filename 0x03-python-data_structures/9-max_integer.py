#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > max_value:
            max_value = i
            return max_value

max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
