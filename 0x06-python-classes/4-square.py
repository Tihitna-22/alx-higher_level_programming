#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """getter of size

        returns:
        the size of square
        """
    @size.setter
    def size(self, value):
        """setter of __size
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
