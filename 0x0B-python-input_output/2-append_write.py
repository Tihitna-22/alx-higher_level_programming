#!/user/bin/python3
""" append function"""


def append_write(filename="", text=""):
    """
    appends a string at the end returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
