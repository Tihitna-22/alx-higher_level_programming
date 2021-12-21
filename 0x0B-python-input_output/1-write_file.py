#!/usr/bin/python3
"""
function writes a string
"""


def write_file(filename="", text=""):
    """writes a strin and eturns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
