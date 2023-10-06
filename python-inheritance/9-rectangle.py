#!/usr/bin/python3
"""
    Class rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle
    """

    def __init__(self, width, height):
        """
            init
        """

        if self.integer_validator("width", width) is True:
            self.__width = width
        if self.integer_validator("height", height) is True:
            self.__height = height

    def area(self):
        """
        Function area not available yet
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
