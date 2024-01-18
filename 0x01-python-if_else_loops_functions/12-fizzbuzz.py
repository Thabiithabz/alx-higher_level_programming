#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 != 0:
            print("fizz ", end='')
        elif x % 5 == 0 and x % 3 != 0:
            print("Buzz ", end='')
        elif x % 5 == 0 and x % 3 == 0:
            print("fizzbuzz ", end='')
        else:
            print("{}".format(x), end='')
