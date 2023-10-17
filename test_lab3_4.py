import unittest
from lab3_4 import ile_wywolana


class TestIleWywolana(unittest.TestCase):

    def test_ile_wywolana_is_generator(self):
        generator = ile_wywolana()
        self.assertTrue(callable(getattr(generator, '__iter__', None)), "Object is not iterable.")
        self.assertTrue(callable(getattr(generator, '__next__', None)), "Object does not have a __next__ method.")
        
    def test_ile_wywolana_values(self):
        generator = ile_wywolana()
        self.assertEqual(next(generator), 1, "First call to ile_wywolana did not return 1")
        self.assertEqual(next(generator), 2, "Second call to ile_wywolana did not return 2")
        self.assertEqual(next(generator), 3, "Third call to ile_wywolana did not return 3")

    def test_ile_wywolana_custom(self):
        generator = ile_wywolana()
        # Test for a higher number
        for _ in range(99):
            next(generator)
        self.assertEqual(next(generator), 100, "Hundredth call to ile_wywolana did not return 100")


if __name__ == "__main__":
    unittest.main()
