#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(1, 2)
        cls.s3 = Square(2, 3, 4)
        cls.s4 = Square(4, 5, 6, 7)

    def test_id(self):
        """Test for id"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 4)

    def test_size(self):
        """Test for size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 1)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s4.size, 4)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 1)
        self.assertEqual(self.s3.width, 2)
        self.assertEqual(self.s4.width, 4)

    def test_height(self):
        """Test for height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 1)
        self.assertEqual(self.s3.height, 2)
        self.assertEqual(self.s4.height, 4)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s4.x, 5)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 4)
        self.assertEqual(self.s4.y, 6)

    def test_size_typeError(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hi")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeError(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hi")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeError(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2, "hi")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2, True)

    def test_size_valueError(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valueError(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(2, -1)

    def test_y_valueError(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 2, -3)

    def test_area(self):
        """test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 1)
        self.assertEqual(self.s3.area(), 4)
        self.assertEqual(self.s4.area(), 16)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 2/0 - 1")
        self.assertEqual(str(self.s3), "[Square] (3) 3/4 - 2")
        self.assertEqual(str(self.s4), "[Square] (4) 5/6 - 4")
