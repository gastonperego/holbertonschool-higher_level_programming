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
            ret.append(dic)

        return json.dumps(ret)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        with open(f"{cls}.json", "w", encoding="utf-8") as file:

            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                file.write(to_json_string(list_objs))

    def from_json_string(json_string):
        """converts a json string into a list"""

        if json_string is None or len(json_string) == 0 or json_string == "":
            return ""
        else:
            return json.loads(json_string)
