#!/usr/bin/python3
"""Append text"""


def append_write(filename="", text=""):
    """Append text"""

    with open(filename, "a", encoding="utf-8") as file:
        num = file.write(text)

    return num
