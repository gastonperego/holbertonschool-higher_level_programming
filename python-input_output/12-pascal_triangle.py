#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""

    if n < 1 or type(n) is not int:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        new_list = [[1, 2, 1]]
        for i in range(0, n - 3):
            new_list.append(add_new_list(new_list[i]))
        new_list.insert(0, [1, 1])
        new_list.insert(0, [1])
        return new_list


def add_new_list(last_list=[]):
    """Adds a new list to the triangle"""

    my_list = [1]
    for i in range(len(last_list) - 1):
        my_list.append(last_list[i] + last_list[i + 1])
    my_list.append(1)
    return my_list
