#!/usr/bin/python3

import random
number = random.randint(-10, 10)
if number < 0:
    print(f"%d is negative" % number)
elif number == 0:
    print(f"%d is zero" % number)
else:
    print(f"%d is positive" % number)
