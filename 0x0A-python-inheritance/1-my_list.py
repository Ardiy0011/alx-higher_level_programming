#!/usr/bin/python3
"""
Module: 1-my_list
"""


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        """
        function that prints the sorted list from the base class
        """
        print(sorted(self))
