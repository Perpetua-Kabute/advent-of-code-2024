import unittest
from ceres_search_for_mas import find_diagonal_mas

class CeresSearchForMasTestCase(unittest.TestCase):
    def test_find_diagonal_mas(self):
        input_matrix = [["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
                        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
                        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
                        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
                        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
                        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
                        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
                        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
                        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
                        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"]]
        result = find_diagonal_mas(input_matrix)
        expected = 9
        self.assertEqual(result, expected)
