#!/usr/bin/python3
"""module to return avaliable lists"""


def lookup(obj):
    """ function returns the list of available attributes and methods of an object"""
    return dir(obj)
