#!/usr/bin/python3



def multiple_returns(sentence):
    length = len(sentence)
    first_char = None
    idx = sentence[0]

    if length > 0:
        first_char = idx

    return length, first_char
