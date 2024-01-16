#!/usr/bin/python3
def fizzbuzz():
    for x in range(1,101):
        """checkfor multiples of 3 and 5and replace with fizzbuzz"""
        if x % 3 == 0 and x % 5 == 0:
            print("{fizzbuzz}", end='')
            fizzbuzz()
