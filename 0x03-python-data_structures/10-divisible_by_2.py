#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    divisible_list = []
    for i in my_list:
        if i % 2 == 0:
            divisible_list.append(True)
        else:
            divisible_list.append(False)
    return divisible_list
