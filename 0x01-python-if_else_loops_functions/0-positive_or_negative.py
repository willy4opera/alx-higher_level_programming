#!/usr/bin/python3
import random
Mynum = random.randint(-10, 10)
if Mynum > 0:
    print(f"{Mynum:d} is positive")
elif Mynum == 0:
    print(f"{Mynum:d} is zero")
else:
    print(f"{Mynum:d} is negative")
