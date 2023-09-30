#!/usr/bin/python3
""" Square  """


class Square:
    """Square with a given size """
    __size = None

    def __init__(self, size=0):
        if isinstance(size, int):
            if size > 0:
                self.__size = size
            else:
                print("size must be >= 0")
        else:
            print("size must be an integer")
            
