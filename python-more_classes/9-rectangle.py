#!/usr/bin/python3
""" Rectangle: empty class"""


class Rectangle:
    """ Rectangle: empty class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
        self.__width = value
        Rectangle.number_of_instances += 1

    print_symbol = "#"

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value=0):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value=0):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width * 2 != 0 and self.height * 2 != 0:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0

    def __str__(self):
        string = ""
        if self.height == 0 or self.width == 0:
            return string

        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = Rectangle.area(rect_1)
        b = Rectangle.area(rect_2)
        if a >= b:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
