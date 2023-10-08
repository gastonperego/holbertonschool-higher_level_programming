#!/usr/bin/python3
"""
    Start of the program
"""


class Student():
    """
        Creation of the class student
    """
    def _init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self._dict_
