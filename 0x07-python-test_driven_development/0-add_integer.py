#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the sum of two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer or b must be an integer')
    elif type(b) is not int and type(a) is not float:
        raise TypeError('a must be an integer or b must be an integer')
    else:
        return int(a) + int(b)
