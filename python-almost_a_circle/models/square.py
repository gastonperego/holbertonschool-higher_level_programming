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

    def update(self, *args, **kwargs):
        """Updates the values of the square"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary"""

        return ({"id": self.id, "x": self.x,
                "size": self.__size, "y": self.y})
