#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        num = my_list.pop(idx)
        print("Element at index {:d} is {}".format(idx, num))


def main():
    my_list = [1, 2, 3, 4, 5]
    idx = (4)
    element_at(my_list, idx)
main()
