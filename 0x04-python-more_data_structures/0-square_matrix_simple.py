#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    
    for string in matrix:
        newer = []
        for i in string:
            calc = i ** 2
            newer.append(calc)
        new_matrix.append(newer)
    return new_matrix
