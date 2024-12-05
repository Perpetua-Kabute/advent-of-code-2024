import unittest
from ceres_search_right import search_horizontal_forward
from ceres_search_right import search_horizontal_backward
from ceres_search_right import search_vertical_upward
from ceres_search_right import search_vertical_downward
from ceres_search_right import search_pos_diagonal_forward
from ceres_search_right import search_pos_diagonal_backward
from ceres_search_right import search_neg_diagonal_forward
from ceres_search_right import search_neg_diagonal_backward
from ceres_search_right import find_total_number_of_words

class CeresSearchRightTestCase(unittest.TestCase):
    
    def test_search_horizontal_forward(self):
        input_matrix = [["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ]
        result = search_horizontal_forward(input_matrix)
        expected = 1
        self.assertEqual(result, expected)

    def test_search_horizontal_backward(self):
        input_matrix = [["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ]
        result = search_horizontal_backward(input_matrix)
        expected = 1
        self.assertEqual(result, expected)

    def test_search_vertical_upwards(self):
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
        result = search_vertical_upward(input_matrix)
        expected = 2
        self.assertEqual(result, expected)

    def test_search_vertical_downwards(self):
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
        result = search_vertical_downward(input_matrix)
        expected = 1
        self.assertEqual(result, expected)
    
    def test_search_pos_diagonal_forward(self):
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
        result = search_pos_diagonal_forward(input_matrix)
        expected = 1
        self.assertEqual(result, expected)

    def test_search_pos_diagonal_backward(self):
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
        result = search_pos_diagonal_backward(input_matrix)
        expected = 4
        self.assertEqual(result, expected)
    
    def test_search_neg_diagonal_forward(self):
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
        result = search_neg_diagonal_forward(input_matrix)
        expected = 4
        self.assertEqual(result, expected)
    
    def test_search_neg_diagonal_backwards(self):
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
        result = search_neg_diagonal_backward(input_matrix)
        expected = 1
        self.assertEqual(result, expected)

    def test_find_total_words(self):
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
        result = find_total_number_of_words(input_matrix)
        expected = 18
        self.assertEqual(result, expected)