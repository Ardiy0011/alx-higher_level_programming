#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if length == '':
        first_char == 'none'
    else:
        return(length, first_char)
