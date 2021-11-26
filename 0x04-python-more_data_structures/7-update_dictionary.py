#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key in a_dictionary:
        if a_dictionary[key] == value:
            return a_dictionary[value]
