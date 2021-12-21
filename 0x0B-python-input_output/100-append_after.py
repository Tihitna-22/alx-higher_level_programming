#!/usr/bin/python3
"""
append after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing "search_string" """
    with open(filename, 'r', encoding='utf-8') as f:
        list = []
        while True:
            line = f.readline()
            if line == "":
                break
            list.append(line)
            if search_string in line:
                list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(list)
