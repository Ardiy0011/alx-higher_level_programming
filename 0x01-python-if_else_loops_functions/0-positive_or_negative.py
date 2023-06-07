#!/usr/bin/python3
import random
number = random.randint(-10, 10)
neg = "negative"
pos = "positive"

if number < 0:
    print(f"{number} is {neg}")
else:
    print(f"{number} is {pos}")
