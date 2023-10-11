#!/usr/bin/python3
"""Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        
        super().__init__(size, size, x, y, id)
        self.__size = size
        
    @property
    def size(self):
        """size"""
        
        return self.__size
    
    @size.setter
    def size(self, value):
        """size setter"""
        
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
        
