#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
print("Hello, World!")
print("I would like to get to know you.")
n = input("What is your name? ")
if n == "Trinity":
    print("What do I need to do to get an A? ")
elif n == "Jared":
    print("I've got a bad feeling about you")
else:
    print("I'm glad to meet you, {}".format(n))