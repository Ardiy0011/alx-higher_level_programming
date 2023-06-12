#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    
    temp_a = 0
    temp_b = 0
    
    if len(tuple_a) >= 2:
        temp_a += tuple_a[0]
        temp_b += tuple_a[1]

    elif len(tuple_a) == 1:
        temp_a += tuple_a[0]

    if len(tuple_b) >= 2:
        temp_a += tuple_b[0]
        temp_b += tuple_b[1]

    elif len(tuple_b) == 1:
        temp_a += tuple_b[0]
    return (temp_a, temp_b)

add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
