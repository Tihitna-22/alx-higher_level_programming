#!/usr/bin/python3


class MyList(list):
    """
    Defines  MyList class hat inherits from list
    """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
