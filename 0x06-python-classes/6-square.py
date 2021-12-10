#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter of size
        returns:
        the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value : position of the square
        Returns:
            None
        """
        if len(value) < 2 or type(value[0]) is not int or \
                type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def my_print(self):
        """print square with # symbol
        Returns:
            The area of the square with #
        """
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
