import unittest
from lab3_3 import zwroc_większe, zwroc_większe_2


def f1(n):
    return n**2-3*n


def f2(n):
    return 100-n


def f3(word):
    return word[::-1]


class TestZwrocWieksze(unittest.TestCase):

    def test_funkcja_f1(self):
        self.assertEqual(zwroc_większe(f1, 4, 6, 2, -5), [6, -5])

    def test_funkcja_f2(self):
        self.assertEqual(zwroc_większe(f2, *range(100)), list(range(50)))

    def test_funkcja_f3(self):
        self.assertEqual(zwroc_większe(f3, "python", "nie", "jest", "bardzo", "fajny"), ['jest', 'bardzo', 'fajny'])

    def test_tuple_packing(self):
        args = (1, 2, 3, 4, 5)
        self.assertEqual(zwroc_większe(lambda x: x + 1, *args), [1, 2, 3, 4, 5])

    def test_puste_argumenty(self):
        self.assertEqual(zwroc_większe(f1), [])


class TestZwrocWieksze(unittest.TestCase):

    def test_funkcja_f1(self):
        self.assertEqual(zwroc_większe_2(f1, 4, -5, 6, 2), [-5])

    def test_funkcja_f2(self):
        self.assertEqual(zwroc_większe_2(f2, *range(100)), [])

    def test_funkcja_f3(self):
        self.assertEqual(zwroc_większe_2(f3, "python", "nie", "jest", "bardzo", "fajny"), ['jest', 'fajny'])

    def test_puste_argumenty(self):
        self.assertEqual(zwroc_większe_2(f1), [])

    def test_brak_argumentow(self):
        self.assertEqual(zwroc_większe_2(lambda x: x), [])

    def test_jeden_argument(self):
        self.assertEqual(zwroc_większe_2(lambda x: x, "tylko jeden"), [])

    def test_ciagi_znakow(self):
        self.assertEqual(zwroc_większe_2(lambda x: len(x), "krotki", "sredni", "najdluzszy"), ["najdluzszy"])


if __name__ == '__main__':
    unittest.main()
