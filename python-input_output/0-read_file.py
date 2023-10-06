#!/usr/bin/python3
"""Read a text file and print it to the stdout"""


def read_file(filename=""):
    """Read a text file and print it to the stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        read_text = file.read()

    print(read_text)
    file.closed
