#!/usr/bin/python3
"""Class for square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y)

    def __str__(self):
        """string representation of the square"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the  size"""
        self.width = value
        self.height = value
