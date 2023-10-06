#!/usr/bin/python3
"""
Class definition base geometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        Function area not available yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates an integer
        """
        if isinstance(name, str):
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
            elif value < 1:
                raise ValueError(f"{name} must be greater than 0")
