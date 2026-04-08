import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual (0, add(-1,1))
        self.assertEqual(7,add(2,5))
        self.assertEqual(-7, add(-2, -5))

    def test_subtract(self): # 3 assertions
        self.assertEqual (5, sub(10,5))
        self.assertEqual(-5, sub(-2,3))
        self.assertEqual(0, sub(-5, -5))

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(3, logarithm(2, 8))
        self.assertEqual(2, logarithm(10,100))
        self.assertEqual(2, logarithm(9,81))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm (1, 2)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()