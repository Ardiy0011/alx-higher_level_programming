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



""" 
task 2

def replace_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list) -1:
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

main() """



""" task 6

def print_matrix_integer(matrix=[[]]):
    for string in matrix:
        for element in string:
            print("{:d}".format(element), end=' ')
        print()

print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer() """