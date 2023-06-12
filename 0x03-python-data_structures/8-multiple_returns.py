#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    idx = sentence[0]
    first_char = None
    if length > 0:
        first_char = idx
    return length, first_char
