#!/usr/bin/python3
"""A"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Function area not available yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
