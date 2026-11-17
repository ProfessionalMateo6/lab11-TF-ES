# https://github.com/ProfessionalMateo6/lab11-TF-ES
# Partner 1: Takumi Fenderson
# Partner 2: Eduardo Silva

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-2, 2), 0)
        self.assertNotEqual(add(-2, 2), 4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, -2), 4)
        self.assertNotEqual(subtract(2, -2), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(-4, 5), -20)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertAlmostEqual(div(2, 7), 3.5)
        self.assertEqual(div(4, -20), -5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(3, 3), 1)
        self.assertEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -2)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12),13)
        self.assertEqual(hypotenuse(7, 24),25)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
# Do not touch this
if __name__ == "__main__":
    unittest.main()