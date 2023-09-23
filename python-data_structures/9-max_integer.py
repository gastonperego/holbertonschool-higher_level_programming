#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    i = 1
    a = my_list[0]
    while i < len(my_list):
        if (my_list[i] > a):
            a = my_list[i]
        i += 1
    return a
