#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base
import json


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints the rectangle with \"#\""""

        position = [self.__x, self.__y]
        if position[1] != 0:
            for i in range(position[1]):
                print()
        for i in range(self.__height):
            print(" " * position[0], end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns something"""

        if type(self) is Rectangle:
            st = f"{self.__width}/{self.__height}"
            return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " + st)
        else:
            string1 = f"{self.__width}"
            return (f"[Square] ({self.id}) {self.__x}/{self.__y} - " + string1)

    def update(self, *args, **kwargs):
        """updates the values of th rectangle"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "width" or key == "_Rectangle__width":
                    self.__width = kwargs[key]
                if key == "height" or key == "_Rectangle__height":
                    self.__height = kwargs[key]
                if key == "x" or key == "_Rectangle__x":
                    self.__x = kwargs[key]
                if key == "y" or key == "_Rectangle__y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """returns dictionary"""

        return self.__dict__
