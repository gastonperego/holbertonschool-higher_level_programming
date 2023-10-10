#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


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

        string = ""
        if self.height == 0 or self.width == 0:
            return string

        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            if i != self.height - 1:
                string += '\n'
        print(string)
    
    def __str__(self):
        """returns something"""

        string1 = f"{self.__width}/{self.__height}"
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " + string1)
