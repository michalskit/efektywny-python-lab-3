import unittest
from lab3_3 import zwroc_rosnace

def f1(n):
    return n**2-3*n


def f2(n):
    return 100-n


def f3(word):
    return word[::-1]


class TestZwrocWieksze(unittest.TestCase):

    def test_funkcja_f1(self):
        self.assertEqual(zwroc_rosnace(f1, 4, 6, 2, -5), [6, -5])

    def test_funkcja_f2(self):
        self.assertEqual(zwroc_rosnace(f2, *range(100)), list(range(50)))

    def test_funkcja_f3(self):
        self.assertEqual(zwroc_rosnace(f3, "python", "nie", "jest", "bardzo", "fajny"), ['jest', 'bardzo', 'fajny'])

    def test_tuple_packing(self):
        args = (1, 2, 3, 4, 5)
        self.assertEqual(zwroc_rosnace(lambda x: x + 1, *args), [1, 2, 3, 4, 5])

    def test_puste_argumenty(self):
        self.assertEqual(zwroc_rosnace(f1), [])


if __name__ == '__main__':
    unittest.main()
