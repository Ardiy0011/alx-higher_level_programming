#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        value = 0
        for i in my_list:
            num += (i[0] * i[1])
            value += (i[1])
        return (num/value)
    return 0