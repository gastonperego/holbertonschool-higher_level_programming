#!/usr/bin/python3
"""convert a json string to normal"""


import json


def from_json_string(my_str):
    """convert a json string to normal"""

    return json.loads(my_str)
