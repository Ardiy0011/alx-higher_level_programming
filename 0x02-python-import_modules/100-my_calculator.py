#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

def calculate(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return None

if __name__ == "__main__":
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = calculate(a, operator, b)
    if result is None:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
