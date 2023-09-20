#!/usr/bin/python3
i = ord('a')
for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        i += 2
    else:
        print("{}".format(chr(i)), end="")
