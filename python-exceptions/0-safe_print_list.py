#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if not my_list or my_list == [] or my_list is None:
        return 0
    a = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            a += 1
        except (TypeError, IndexError):
            pass
    print()
    return a
