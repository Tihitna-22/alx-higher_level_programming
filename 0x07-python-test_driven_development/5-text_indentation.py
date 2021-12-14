#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        new_line = True
        for elm in range(0, len(text)):
            if new_line is True and text[elm] == ' ':
                print(end="")
            elif text[elm] == '.' or text[elm] == '?' or text[elm] == ':':
                print(text[elm] + "\n")
                new_line = True
            else:
                print(text[elm], end="")
                new_line = False
