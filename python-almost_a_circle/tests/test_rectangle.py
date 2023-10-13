"""Rectangle test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class RectangleTests(unittest.TestCase):

    def test_only_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)
        
    def test_no_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
    
    def test_print_private_attribute_1(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__width)

    def test_print_private_attribute_2(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__height)

    def test_print_private_attribute_3(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__x)

    def test_print_private_attribute_4(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_getter_works_1(self):
        r1 = Rectangle(2, 2, 2, 2)
        self.assertEqual(2, r1.width)

    def test_getter_works_1(self):
        r1 = Rectangle(2, 2, 2, 2)
        self.assertEqual(2, r1.height)

    def test_getter_works_1(self):
        r1 = Rectangle(2, 2, 2, 2)
        self.assertEqual(2, r1.x)

    def test_getter_works_1(self):
        r1 = Rectangle(2, 2, 2, 2)
        self.assertEqual(2, r1.y)
   