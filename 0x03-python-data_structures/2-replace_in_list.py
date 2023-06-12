#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

def main():
    my_list = [2, 4, 6, 8, 10]
    idx = (3)
    element = (9)
    new_list = replace_in_list(my_list, idx, element)
    print(new_list)
    print(my_list)

main()
