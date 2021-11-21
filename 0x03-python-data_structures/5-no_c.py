#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for str in my_string:
        if str != 'c' and str != 'C':
            new_string += str
    return new_string
