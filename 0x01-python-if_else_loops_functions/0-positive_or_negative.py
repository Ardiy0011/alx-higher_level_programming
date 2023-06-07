#!/usr/bin/python3
import random
number = random.randint(-10, 10)
neg = "negative"
pos = "positive"
zer = "zero"

if number < 0:
    print(f"{number} is {neg}")
elif number == 0:
    print(f"{number} is {zer}")
else:
    print(f"{number} is {pos}")
