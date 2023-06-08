#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import addin, subin, multin, diving
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, addin(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, subin(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, multin(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, int(diving(a, b))),end='')
