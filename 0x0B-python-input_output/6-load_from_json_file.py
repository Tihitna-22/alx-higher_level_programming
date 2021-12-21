#!/usr/bin/python3
"""
function load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.loads(myFile.read())
