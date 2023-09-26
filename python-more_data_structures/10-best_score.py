#!/usr/bin/python3

def best_score(a_dictionary):

    tmp = 0
    value = []
    if a_dictionary == [] or a_dictionary is None:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > tmp:
            tmp = a_dictionary[i]
            value = i
    return value
