#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        return a / b
        if b == 0:
            raise ZeroDivisionError()
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        return


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))