#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, val in a_dictionary.items():
        new_dictionary[key] = 2 * val
    return new_dictionary
