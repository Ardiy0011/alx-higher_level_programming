#!/usr/bin/python3
def uppercase(string):
    for i in string:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()


uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
