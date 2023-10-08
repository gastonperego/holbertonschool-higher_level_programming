#!/usr/bin/python3
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

    def reload_from_json(self, json):
        """reloads from json"""

        my_list = []
        for i in json:
            my_list.append(json[i])
        self.__init__(my_list[0], my_list[1], my_list[2])
