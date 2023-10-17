import unittest
from lab3_2 import numbers_to_percents


class TestNumbersToPercents(unittest.TestCase):

    def test_basic_list(self):
        self.assertEqual(numbers_to_percents([1, 2, 1]), [0.25, 0.5, 0.25])

    def test_single_item_list(self):
        self.assertEqual(numbers_to_percents([1]), [1])

    def test_different_numbers(self):
        self.assertEqual(numbers_to_percents([1, 2, 3, 4]), [0.1, 0.2, 0.3, 0.4])

    def test_empty_list(self):
        self.assertEqual(numbers_to_percents([]), [])

    def test_list_of_zeros(self):
        self.assertEqual(numbers_to_percents([0, 0, 0]), [0, 0, 0])

    def test_with_generator(self):
        numbers = (x for x in [1, 2, 3, 4]) 
        self.assertEqual(numbers_to_percents(numbers), [0.1, 0.2, 0.3, 0.4])

    def test_mixed_numbers(self):
        self.assertEqual(numbers_to_percents([1, -1, 2, -2]), [0.16666666666666666, -0.16666666666666666, 0.3333333333333333, -0.3333333333333333])

    def test_negative_numbers(self):
        self.assertEqual(numbers_to_percents([-1, -2, -3, -4]), [-0.1, -0.2, -0.3, -0.4])


if __name__ == '__main__':
    unittest.main()
