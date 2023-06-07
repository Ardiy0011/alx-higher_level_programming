#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print("{}".format(str(a).zfill(2)), end=' ')
    else:
        print("{},".format(str(a).zfill(2)), end=' ') 

  