import unittest
from lab3_1 import mean, check_dictionary_content

class TestMeanFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean(1, 2, 3), 2)

    def test_even_numbers(self):
        self.assertEqual(mean(2, 2, 4, 4), 3)

    def test_various_numbers(self):
        self.assertAlmostEqual(mean(1, 2, 3, 4, 5, 61, 2, 12, 123, 123), 33.6)

    def test_single_number(self):
        self.assertEqual(mean(5), 5)

    def test_zero(self):
        self.assertEqual(mean(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(mean(-1, -2, -3), -2)

    def test_mixed_numbers(self):
        self.assertEqual(mean(-1, 2, -3, 4), 0.5)

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            mean(1, 2, '3', 4)

    def test_tuple_packing(self):
        numbers = (1, 2, 3)
        self.assertEqual(mean(*numbers), 2)


class TestCheckDictionaryContent(unittest.TestCase):

    def test_existing_items(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertTrue(check_dictionary_content(d, orange=2))
        self.assertTrue(check_dictionary_content(d, orange=2, apple=1))

    def test_item_with_greater_value(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertFalse(check_dictionary_content(d, dogs=11))

    def test_non_existing_item(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertFalse(check_dictionary_content(d, cats=1))

    def test_non_existing_item_with_zero_value(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertTrue(check_dictionary_content(d, dogs=9, cats=0))

    def test_with_all_false_conditions(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertFalse(check_dictionary_content(d, apple=0, cats=1))

    def test_dictionary_unpacking(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertTrue(check_dictionary_content(d, **d))

    def test_empty_kwargs(self):
        d = {'orange': 3, 'apple': 1, 'dogs': 10}
        self.assertTrue(check_dictionary_content(d))

    def test_empty_dictionary(self):
        d = {}
        self.assertFalse(check_dictionary_content(d, orange=1))


if __name__ == '__main__':
    unittest.main()
