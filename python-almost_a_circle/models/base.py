#!/usr/bin/python3
"""Basae class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None and type(id) is int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return a json string of a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        ret = []
        for dic in list_dictionaries:
            ret.append(str(dic))

        return json.dumps(ret)
