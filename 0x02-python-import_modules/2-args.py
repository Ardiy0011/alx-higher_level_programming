#!/usr/bin/python3

def arglist(argv):
    length = len(argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length))
        i = 1
        while i <= length:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    arglist(sys.argv)
