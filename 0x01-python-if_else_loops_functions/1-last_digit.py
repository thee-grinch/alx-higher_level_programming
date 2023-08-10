#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
if number < 0:
    number = 0 - number
    n = number % 10
    n = -n
else:
    n = number % 10
if n > 5:
    print(f"{n} and is greater than 5")
elif n == 0:
    print(f"{n} and is 0")
else:
    print(f"{n} and is less than 6 and not 0")
