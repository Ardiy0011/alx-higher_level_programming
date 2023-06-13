#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = [x for x in my_list]
    if idx < 0 or idx >= len(new_list):
        return my_list
    else:
        new_list.remove(new_list[idx])
        my_list.remove(my_list[idx])
    return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
