#!/usr/bin/python3
"""
   Function that finds a peak in a list of unsorted integers
"""

def find_peak(numbr):
    '''
        Finds the peak in a list of unsorted numbers
    '''
    length = len(numbr)
    if length == 0:
        return None
    if length == 1:
        return numbr[0]
    if length == 2:
        return max(numbr[0], numbr[1])

    for index in range(length):
        value = numbr[index]
        if (index > 0 and index < length - 1 and
                numbr[index + 1] <= value and numbr[index - 1] <= value):
                return value
        elif index == 0 and numbr[index + 1] <= value:
            return value
        elif index == length - 1 and numbr[index - 1] <= value:
            return value
    return None
