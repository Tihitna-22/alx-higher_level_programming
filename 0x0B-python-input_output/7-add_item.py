#!/usr/bin/python3
"""
function adds all arguments to a Python list, and then saves them to a file
"""
from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    list = load_from_json_file("add_item.json")
except:
    list = []

for arg in argv[1:]:
    list.append(arg)

save_to_json_file(list, "add_item.json")
