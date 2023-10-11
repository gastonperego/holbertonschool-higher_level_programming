"""Rectangle test"""
import unittest


class RectangleTests(unittest.TestCase):
    
    def full_rectangle(self):
        self.assertTrue(3, 4, 5, 2, 12)
        
    def no_id(self):
        self.assertTrue(3, 4, 5, 2)
        
    def args_3(self):
        self.assertTrue(3, 4, 5)
        
    def args_2(self):
        self.assertTrue(3, 4)
    
    def only_arg(self):
        self.assertFalse(3)
        
    def no_args(self):
        self.assertFalse()
   