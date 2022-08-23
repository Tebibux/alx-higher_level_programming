#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numStr = str(number)
lsDg = int(numStr[-1])
if ((lsDg < 5) and (lsDg != 0)):
    print(f'Last digit of {number} is {lsDg} and is less than 6 and not 0')
elif lsDg == 0:
    print(f'Last digit of {number} is {lsDg} and is 0')
else:
    print(f'Last digit of {number} is {lsDg} and is greater than 5')
