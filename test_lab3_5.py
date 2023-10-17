import unittest
from lab3_5 import get_primes


class TestGetPrimes(unittest.TestCase):
    def test_primes(self):
        generator = get_primes(1)
        # Sprawdź, czy pierwsze wartości zwracane przez generator to rzeczywiście liczby pierwsze.
        self.assertEqual(next(generator), 2)
        self.assertEqual(next(generator), 3)
        self.assertEqual(next(generator), 5)
        self.assertEqual(next(generator), 7)
        self.assertEqual(next(generator), 11)

    def test_is_generator(self):
        # Sprawdź, czy obiekt zwracany przez funkcję jest rzeczywiście generatorem.
        generator = get_primes(1)
        self.assertTrue(callable(getattr(generator, '__iter__', None)))
        self.assertTrue(callable(getattr(generator, '__next__', None)))


if __name__ == "__main__":
    unittest.main()
