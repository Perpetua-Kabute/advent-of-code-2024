import unittest
from ceres_search import find_xmas_from_word_search
from ceres_search import find_xmas_horizontally
from ceres_search import find_xmas_vertically
from ceres_search import find_xmas_diagonally
from ceres_search import transform_matrix_to_string

class CeresSearchTestCase(unittest.TestCase):
    def test_find_horizontal_xmas(self):
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
        result = find_xmas_horizontally(transform_matrix_to_string(input_matrix))
        expected = 5
        self.assertEqual(result, expected)
    def test_find_xmas_vertically(self):
        result = find_xmas_vertically([
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
        ])
        expected = 3
        self.assertEqual(result, expected)

    def test_find_xmas_diagonally(self):
        result = find_xmas_diagonally([
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
        ])
        expected = 10
        self.assertEqual(result, expected)
    def test_find_xmas_from_word_search(self):
        matrix =[["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
                 ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
                 ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
                 ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
                 ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
                 ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
                 ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
                 ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
                 ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
                 ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"]]
        result = find_xmas_from_word_search(matrix)
        expected = 18
        self.assertEqual(result, expected)