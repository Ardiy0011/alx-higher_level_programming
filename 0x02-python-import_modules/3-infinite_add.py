#!/usr/bin/python3

def arglist(argv):
    length = len(argv) - 1
    total = 0


    i = 1

    while i <= length:
        total += int(argv[i])
        i += 1
    print(total)


if __name__ == "__main__":
    import sys
    arglist(sys.argv)
