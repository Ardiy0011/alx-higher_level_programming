#!/usr/bin/python3

def common_is(set_1, set_2):
    var = set_1 | set_2
    for i in set_1:
        if i in set_2:
            var.remove(i)
    return var
