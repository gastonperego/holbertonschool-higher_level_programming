#!/usr/bin/python
"""class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict"""

        new_dict = {}
        if type(attrs) is list and all(isinstance(i, str) for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

        else:
            return (self.__dict__)
