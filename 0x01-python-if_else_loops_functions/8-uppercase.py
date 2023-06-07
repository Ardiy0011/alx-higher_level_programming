#!/usr/bin/python3
def uppercase(string):
    for i in string:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()
