import unittest
import types
from lab3_6 import natural_numbers, factorials

class NaturalNumbersTest(unittest.TestCase):

    def test_is_generator(self):
        self.assertIsInstance(natural_numbers(), types.GeneratorType)

    def test_values_from_zero(self):
        gen = natural_numbers()
        for i in range(21):
            self.assertEqual(next(gen), i)

    def test_values_from_one(self):
        gen = natural_numbers(1)
        for i in range(1, 22):
            self.assertEqual(next(gen), i)

class FactorialsTest(unittest.TestCase):

    def test_is_generator(self):
        self.assertIsInstance(factorials(), types.GeneratorType)

    def test_factorial_values(self):
        gen = factorials()
        expected_results = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        for expected in expected_results:
            self.assertEqual(next(gen), expected)

if __name__ == '__main__':
    unittest.main()
