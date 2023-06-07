#!/usr/bin/python3
for i in range(ord('a'), ord('y') + 2):
    if chr(i) == 'q':
        continue
    if chr(i) == 'e':
        continue
    print("{}".format(chr(i)), end='')
