#!/usr/bin/python3
import random
number = random.randint(-10, 10)
neg = "negative"
pos = "positive"

#if number is negative print variable neg else if positive print varibale pos
if number < 0:
    print(f"{number} is {neg}")
else:
    print(f"{number} is {pos}")
