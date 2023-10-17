import unittest
import types
from lab3_7 import fibonacci


class TestFibonacciGenerator(unittest.TestCase):

    def test_generator_instance(self):
        # Sprawdzenie, czy zwrócona wartość jest instancją generatora
        fib = fibonacci()
        self.assertIsInstance(fib, types.GeneratorType)

    def test_fibonacci_sequence(self):
        # Sprawdzenie, czy pierwsze pięć wartości zwróconych przez generator to poprawny ciąg Fibonacciego
        fib = fibonacci()
        expected_sequence = [0, 1, 1, 2, 3]
        generated_sequence = [next(fib) for _ in range(5)]
        self.assertEqual(expected_sequence, generated_sequence)

if __name__ == '__main__':
    unittest.main()
