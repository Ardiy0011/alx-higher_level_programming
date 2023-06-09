#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def main():
    length = len(sys.argv) - 1
    maths = {'+': add, '-': sub, '*': mul, '/': div}

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in maths:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, operator, b = map(int, sys.argv[1:])
    result = maths[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    main()
