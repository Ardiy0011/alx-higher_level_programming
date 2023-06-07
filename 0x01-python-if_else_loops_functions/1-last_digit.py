#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
greater = "and is greater than 5"
lower = "and is less than 6 and not 0"
zer = "and is 0"

if number < 0:
    last = -(abs(number) % 10)
if last > 5:
    print(f"last digit of {number} is {last} {greater}")
elif last == 0:
    print(f"last digit of {number} is {last} {zer}")
elif last < 6 and last != 0:
    print(f"last digit of {number} is {last} {lower}")
else:
    print(f"last digit of {number} is -{last} {lower}")
