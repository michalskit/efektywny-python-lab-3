import unittest
from lab3_2 import numbers_to_percents


class TestNumbersToPercents(unittest.TestCase):

    def test_basic_list(self):
        self.assertEqual(numbers_to_percents([1, 2, 1]), [25.0, 50.0, 25.0])

    def test_single_item_list(self):
        self.assertEqual(numbers_to_percents([1]), [100.0])

    def test_different_numbers(self):
        self.assertEqual(numbers_to_percents([1, 2, 3, 4]), [10.0, 20.0, 30.0, 40.0])

    def test_empty_list(self):
        self.assertEqual(numbers_to_percents([]), [])

    def test_list_of_zeros(self):
        self.assertEqual(numbers_to_percents([0, 0, 0]), [])

    def test_with_generator(self):
        numbers = (x for x in [1, 2, 3, 4])
        self.assertEqual(numbers_to_percents(numbers), [10.0, 20.0, 30.0, 40.0])

    def test_mixed_numbers(self):
        result = numbers_to_percents([1, -1, 2, -2])
        expected = [16.67, 16.67, 33.33, 33.33]
        self.assertTrue(all(abs(a-b) < 0.01 for a, b in zip(result, expected)), 
                        f"Expected {expected}, but got {result}")

    def test_negative_numbers(self):
        self.assertEqual(numbers_to_percents([-1, -2, -3, -4]), [10.0, 20.0, 30.0, 40.0])


if __name__ == '__main__':
    unittest.main()
