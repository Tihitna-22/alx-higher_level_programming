#!/usr/bin/python3
"""Class for square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the  size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id,
                        self.x,
                        self.y,
                        self.width)

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            item = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, item[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
