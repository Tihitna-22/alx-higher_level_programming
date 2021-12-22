#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
