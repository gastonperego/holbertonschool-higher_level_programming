#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * -1
last = number % 10
if last <= 5 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last % 10 > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
else:
    print(f"Last digit of {number} is {last} and is zero")
