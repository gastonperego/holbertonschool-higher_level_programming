#!/usr/bin/python3
"""write text to a file"""


def write_file(filename="", text=""):
    """write text to a file"""

    with open(filename, "w", encoding="utf-8")as file:
        num = file.write(text)

    return num
