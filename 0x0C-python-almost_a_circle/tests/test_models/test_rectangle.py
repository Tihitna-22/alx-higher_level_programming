import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test the functionality of the Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(5, 6)
        cls.r2 = Rectangle(1, 2, 3)
        cls.r3 = Rectangle(3, 4, 5, 6, 7)
        cls.r4 = Rectangle(7, 8, 9, 10)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 7)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r4.width, 7)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 4)
        self.assertEqual(self.r4.height, 8)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.x, 5)
        self.assertEqual(self.r4.x, 9)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 6)
        self.assertEqual(self.r4.y, 10)

    def test_width_typeerror(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hi", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_height_typeerror(self):
        """Test non-ints for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hi")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, "hi")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(5, 5, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, True)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 4)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.r1.area(), 30)
        self.assertEqual(self.r2.area(), 2)
        self.assertEqual(self.r3.area(), 12)
        self.assertEqual(self.r4.area(), 56)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 5/6")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 3/0 - 1/2")
        self.assertEqual(str(self.r3), "[Rectangle] (7) 5/6 - 3/4")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 9/10 - 7/8")

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
