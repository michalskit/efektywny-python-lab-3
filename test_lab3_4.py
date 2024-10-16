import unittest
from lab3_4 import ile_wywolana


class TestIleWywolana(unittest.TestCase):

    def setUp(self):
        ile_wywolana.counter = 0  # Reset counter before each test

    def test_ile_wywolana_is_function(self):
        self.assertTrue(callable(ile_wywolana), "ile_wywolana should be a callable function")

    def test_ile_wywolana_values(self):
        self.assertEqual(ile_wywolana(), 1, "First call to ile_wywolana did not return 1")
        self.assertEqual(ile_wywolana(), 2, "Second call to ile_wywolana did not return 2")
        self.assertEqual(ile_wywolana(), 3, "Third call to ile_wywolana did not return 3")

    def test_ile_wywolana_custom(self):
        for i in range(1, 100):
            self.assertEqual(ile_wywolana(), i, f"Call {i} to ile_wywolana did not return {i}")


if __name__ == "__main__":
    unittest.main()
