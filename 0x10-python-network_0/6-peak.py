#!/usr/bin/python3
"""
   Function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers)
    '''
        Finds the peak in a list of unsorted numbers
    '''
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers[0], list_of_integers[1])

    for index in range(length):
        value = list_of_integers[index]
        if (index > 0 and index < length - 1 and
                list_of_integers[index + 1] <= value and list_of_integers[index - 1] <= value):
                return value
        elif index == 0 and list_of_integers[index + 1] <= value:
            return value
        elif index == length - 1 and list_of_integers[index - 1] <= value:
            return value
    return None
