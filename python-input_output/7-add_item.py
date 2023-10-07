#!/usr/bin/python3
"""add arguments to a list"""

from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    my_list = load_from_json_file("add_item.json")

except:
    my_list = []
finally:
    with open("add_item.json", "w", encoding="utf-8"):
        for i in range(1, len(argv)):
            my_list.append(argv[i])
        save_to_json_file(my_list, "add_item.json")
