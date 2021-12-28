#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""
from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter od width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns:the area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character-#"""
        for i in range(self.__y):
            print()
        for j in range(self.height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        "returns string"
        s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return s.format(self.id,
                        self.__x,
                        self.__y,
                        self.__width,
                        self.__height)

    def update(self, *args, **kwargs):
        """update the instance attributes"""
        if args:
            item = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, item[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
                'x': self.__x,
                'y': self.__y,
                'height': self.__height,
                'width': self.__width}
