""" Tests """
import unittest

class BaseTests(unittest.TestCase):
    """Base test"""
    
    def normal_input(self):
        self.assertTrue(12)
        
    def empty_input(self):
        self.assertEqual(id)
        
