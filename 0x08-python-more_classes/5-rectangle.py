#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Defines the implementation of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property retriever"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter, for setting"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property retriever,to get
        the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.
        Returns:
            The perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the class as a rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i is not self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """Returns string representation of rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a string when an instance of rectangle deleted """
        print("Bye rectangle...")
