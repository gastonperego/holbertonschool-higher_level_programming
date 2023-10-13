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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string of a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        ret = []
        for dic in list_dictionaries:
            ret.append(dic)

        return json.dumps(ret)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if list_objs is None or len(list_objs) == 0:
            ret = []
        else:
            ret = []
            for obj in list_objs:
                ret.append(obj.to_dictionary())

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(ret))

    def from_json_string(json_string):
        """converts a json string into a list"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        print(cls)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 3, 4)
        elif cls.__name__ == "Square":
            dummy = cls(1, 2, 2, 4)
        else:
            return
        dummy.update(**dictionary)
        return dummy
