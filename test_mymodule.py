"""
Test case
"""

import unittest

from mymodule import square, doubler
class TestMyModule(unittest.TestCase):
    def test_square(self):
        """Testing if the function is correct"""
        self.assertEqual(square(2), 4)
         
    def test_doubler(self):
        """Testing if the function is correct"""
        self.assertEqual(doubler(0) , 0)
         
if __name__=='__main__':
    unittest.main()
    
         