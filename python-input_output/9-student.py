#!/usr/bin/python
"""class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """rat"""

        return (self.__dict__)
