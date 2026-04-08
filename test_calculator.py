import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-5, 5), -25)
        self.assertEqual(multiply(0, 1), 0)
    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 6), 3)
        self.assertAlmostEqual(divide(4, 10), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 7)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(-5,12), 13)
        with self.assertRaises(ValueError):
            hypotenuse("1","2")

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        # Test basic function
        self.assertEqual(square_root(16),4)
        self.assertAlmostEqual(square_root(2), 1.41, places=2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()