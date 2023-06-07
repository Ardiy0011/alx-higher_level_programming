#!/usr/bin/python3
for firstcombo in range(9):
    for seccombo in range(firstcombo + 1, 10):
        if firstcombo == 8 and seccombo == 9:
            print("{}{}".format(firstcombo, seccombo))
        else:
            print("{}{},".format(firstcombo, seccombo), end=' ')
