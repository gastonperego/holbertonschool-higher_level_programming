#!/usr/bin/python3

def no_c(my_string):
    i = 0
    list1 = list(my_string)
    while i < len(my_string):
        if my_string[i] == "c" or my_string[i] == "C":
            list1[i] = ""
        i += 1
    my_string = ''.join(list1)
    return my_string
