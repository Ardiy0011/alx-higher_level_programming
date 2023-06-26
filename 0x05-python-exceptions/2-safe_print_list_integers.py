#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        num_e = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            num_e += 1
        if num_e == 0:
            raise ValueError("IndexError: list index out of range")
    except (IndexError, ValueError) as e:
        print(e)
    print()
    return num_e



my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))