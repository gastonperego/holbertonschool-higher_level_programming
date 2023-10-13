""" Tests """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class BaseTests(unittest.TestCase):
    """Base test"""
    
    def test_no_id_given(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        
    def test_id_given(self):
        b1 = Base(4)
        self.assertEqual(4, b1.id)

    def test_print_nb_objects(self):
        b1 = Base()
        b2 = Base(12)
        with self.assertRaises(AttributeError):
            print(b2.nb_objects)
        
    def test_print___nb_objects(self):
        b1 = Base()
        b2 = Base(12)
        with self.assertRaises(AttributeError):
            print(b2.__nb_objects)
    
