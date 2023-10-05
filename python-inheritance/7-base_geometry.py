#!/usr/bin/python3
"""s"""


class BaseGeometry:
    """a"""

    def area(self):
        """a"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a"""
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
