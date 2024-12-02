import unittest
from red_nosed_reports import find_safe_reports
from red_nosed_reports import is_gradual_dampened

class RedNosedReportsTestCase(unittest.TestCase):
    def test_is_increasing_or_decreasing_gradually(self):
        result = is_gradual_dampened([7,6,4,2,1])
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_second(self):
        result = is_gradual_dampened([1,2,7,8,9])
        expected = False
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_third(self):
        result = is_gradual_dampened([9,7,6,2,1])
        expected = False
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_fourth(self):
        result = is_gradual_dampened([1,3,2,4,5])
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_fifth(self):
        result = is_gradual_dampened([8,6,4,4,1])
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_sixth(self):
        result = is_gradual_dampened([1,3,6,7,9])
        expected = True
        self.assertEqual(result, expected)
    def test_increasing_last(self):
        result = is_gradual_dampened([76,79,80,83,85,86,88])
        expeced = True
        self.assertEqual(result,expeced)

    def test_increasing_remove_first(self):
        result = is_gradual_dampened([55,52,53,54,56,57])
        expeced = True
        self.assertEqual(result,expeced)

    def test_decreasing_remove_first(self):
        result = is_gradual_dampened([52,53,52,51,50])
        expeced = True
        self.assertEqual(result,expeced)
    def test_edcase_1(self):
        result = is_gradual_dampened([48, 46, 47, 49, 51, 54, 56])
        expeced = True
        self.assertEqual(result,expeced)
    def test_edcase_2(self):
        result = is_gradual_dampened([1, 1, 2, 3, 4, 5])
        expeced = True
        self.assertEqual(result,expeced)

    def test_edcase_3(self):
        result = is_gradual_dampened([1, 2, 3, 4, 5, 5])
        expeced = True
        self.assertEqual(result,expeced)

    def test_edcase_4(self):
        result = is_gradual_dampened([5, 1, 2, 3, 4, 5])
        expeced = True
        self.assertEqual(result,expeced)
    def test_edcase_5(self):
        result = is_gradual_dampened([1, 4, 3, 2, 1])
        expeced = True
        self.assertEqual(result,expeced)

    def test_edcase_6(self):
        result = is_gradual_dampened([5,4,5,3,2])
        expeced = True
        self.assertEqual(result,expeced)
    def test_red_nosed_reports_first(self):
        result = find_safe_reports([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]])
        expected = 4
        self.assertEqual(result,expected)