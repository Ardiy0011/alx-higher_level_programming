#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    ints = 0
    try:
        for index in range(x):
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end='')
                ints += 1
            else:
                index += 1
        print()
    except (ValueError, TypeError):
        pass
    return ints
