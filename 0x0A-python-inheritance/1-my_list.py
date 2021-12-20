class MyList(list):
    """
    Defines  MyList class hat inherits from list
    """


    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
