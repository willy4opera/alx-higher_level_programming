#!/usr/bin/python3

def fizzbuzz():
    for Mynum in range(1, 101):
        if Mynum % 3 == 0 and Mynum % 5 == 0:
            print("FizzBuzz ", end="")
        elif Mynum % 3 == 0:
            print("Fizz ", end="")
        elif Mynum % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(Mynum), end="")
