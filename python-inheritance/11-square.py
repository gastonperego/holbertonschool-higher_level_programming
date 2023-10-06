#!/usr/bin/python3
"""Class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size):
        """init"""

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Function area not available yet
        """
        return self.__size * self.__size
