#!/usr/bin/python3
"""Checker la recalcada concha de tu madre"""


class BaseGeometry:
    """Checker la recalcada concha de tu madre"""

    def area(self):
        """Checker la recalcada concha de tu madre"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checker la recalcada concha de tu madre"""
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
