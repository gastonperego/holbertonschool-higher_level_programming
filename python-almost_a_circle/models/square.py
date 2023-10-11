#!/usr/bin/python3
"""Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
            self.width = value
            self.height = value
