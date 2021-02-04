import unittest

from calculator import division 
from calculator import multiplication
from calculator import subtraction
from calculator import addition

class TestAverage(unittest.TestCase):
   
    def testDiv (self):
        self.assertEqual(division(10, 2), 5.0)
    def testDiv2 (self):
        self.assertEqual(division(20, 0), 'Value must be greater than zero')
    def testDiv3 (self):
        self.assertEqual(division(12.5, 3.5), 4.0)
    def testDiv4 (self):
        self.assertEqual(division('String', 3.5), 'String values not allowed')

    def testMul (self):
        self.assertEqual(multiplication(10, 2), 20.0)
    def testMul2 (self):
        self.assertEqual(multiplication(20, 0), 0.0)
    def testMul3 (self):
        self.assertEqual(multiplication(-12.5, 3.5), -43.75)
    def testMul4 (self):
        self.assertEqual(multiplication('String', 3.5), 'String values not allowed')

    def testAdd (self):
        self.assertEqual(addition(10, 2), 12.0)
    def testAdd2 (self):
        self.assertEqual(addition(20, 0), 20.0)
    def testAdd3 (self):
        self.assertEqual(addition(-12.5, 3.5), -9.0)
    def testAdd4 (self):
        self.assertEqual(addition('String', 3.5), 'Must be non string input')
    
        
    def testSub (self):
        self.assertEqual(subtraction(10, 2), 8.0)
    def testSub2 (self):
        self.assertEqual(subtraction(20, 0), 20.0)
    def testSub3 (self):
        self.assertEqual(subtraction(-12.5, 3.5), -16.0)
    def testSub4 (self):
        self.assertEqual(subtraction('String', 3.5), 'Must be non string input')
        
        
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        