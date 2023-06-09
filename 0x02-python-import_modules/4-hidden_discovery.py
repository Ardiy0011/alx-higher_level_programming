#!/usr/bin/python3
import hidden_4


def discovr():
    secret = dir(hidden_4)
    for a in secret:
        if a[:2] != '__':
            print(a)


if __name__ == "__main__":
    discovr()
