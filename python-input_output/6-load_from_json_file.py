#!/usr/bin/python3
"""create an object from a json file"""


import json


def load_from_json_file(filename):
    """create an object from a json file"""

    with open(filename, "r", encoding="utf-8") as file:
        obj = json.load(file)

    return obj
