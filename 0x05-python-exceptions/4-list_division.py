#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0

    if list_length <= 0:
        print("out of range")
        return new_list

    while i < list_length:
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            divide = num1 / num2
            new_list.append(divide)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            i += 1

    return new_list
