"""task 0


def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
        
     def main():
    my_list = [1,2,3,4,5]
    print_list_integer(my_list)
main() """


""" task 1

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
main() """
