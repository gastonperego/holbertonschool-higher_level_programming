#!/usr/bin/python3

def safe_print_integer(value):
    try:
        value.isdigit
        a = int(value)
        print("{:d}".format(a))
        return True
    except (ValueError, AttributeError):
        return False
