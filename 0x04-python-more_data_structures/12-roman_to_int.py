#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    num = 0
    dictionary = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1}
    for elem in reversed(roman_string):
        if dictionary[elem] < num:
            res -= dictionary[elem]
        else:
            res += dictionary[elem]
        num = dictionary[elem]
    return res
