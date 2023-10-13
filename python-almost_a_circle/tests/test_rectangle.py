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
        
   