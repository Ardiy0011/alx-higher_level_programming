#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print("{}".format(str(a).zfill(2)))
    else:
        print("{},".format(str(a).zfill(2)), end=' ')
