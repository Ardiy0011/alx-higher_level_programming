#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as er:
        print("Exception: {}".format(er), file=sys.stderr)
    else:
        return None
