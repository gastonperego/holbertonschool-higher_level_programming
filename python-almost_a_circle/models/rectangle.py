#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        id = super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter"""

        return self.__width

    @width.setter

    def width(self, value):
        """setter"""

        if type(value) is int and value >= 0:
            self.__width = value

    @property
    def height(self):
        """getter"""

        return self.__height

    @height.setter

    def height(self, value):
        """setter"""

        if type(value) is int and value >= 0:
            self.__height = value

    @property
    def x(self):
        """getter"""

        return self.__x

    @x.setter

    def x(self, value):
        """setter"""

        if type(value) is int and value >= 0:
            self.__x = value

    @property
    def y(self):
        """getter"""

        return self.__y

    @y.setter

    def y(self, value):
        """setter"""

        if type(value) is int and value >= 0:
            self.__y = value
