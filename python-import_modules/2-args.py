#!/usr/bin/python3

from sys import *

if len(argv) == 1:
    print(f"0 arguments.")
elif len(argv) == 2:
    print(f"1 argument:\n1: {argv[1]}")
else:
    print(f"{len(argv) - 1} arguments:")
    i = 1
    while i < len(argv):
        print(f"{i}: {argv[i]}")
        i += 1