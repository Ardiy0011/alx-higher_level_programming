#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        q = add(a, b)
        for n in range(4, 6):
            q = add(q, n)
        return q
    else:
        return sub(a, b)
