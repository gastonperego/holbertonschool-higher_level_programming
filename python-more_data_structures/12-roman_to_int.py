#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0
    for i in range(0, len(roman_string)):
        for j in dic:
            if roman_string[i] == j:
                res += dic[j]
        if i > 0 and roman_string[i - 1] and dic[roman_string[i - 1]] < dic[roman_string[i]]:
            res -= dic[roman_string[i - 1]] * 2

    return res
