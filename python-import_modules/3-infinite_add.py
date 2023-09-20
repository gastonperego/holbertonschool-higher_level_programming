#!/usr/bin/python3

from sys import *

result = 0
i = 1
if len(argv) == 1:
    pass
else:
    while i < len(argv):
        result += int(argv[i])
        i += 1
print(result)