import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(self,5, 4), 9)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self,9, 4), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(self,13, 4), 52)

    def test_divison(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(self,17, 0)
        self.assertEqual(self.calc.divide(self,17, 4), 4.25)


if __name__ == '__main__':
    unittest.main()