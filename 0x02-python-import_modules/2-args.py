#!/usr/bin/python3

def arglist(argv):
    length = len(argv) - 1
    if length == 0:
        print("{} argument.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    import sys
    arglist(sys.argv)
