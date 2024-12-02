import unittest
from red_nosed_reports import find_safe_reports
from red_nosed_reports import is_increasing_or_decreasing_gradually_dampened

class RedNosedReportsTestCase(unittest.TestCase):
    def test_is_increasing_or_decreasing_gradually(self):
        result = is_increasing_or_decreasing_gradually_dampened([7,6,4,2,1], False)
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_second(self):
        result = is_increasing_or_decreasing_gradually_dampened([1,2,7,8,9], False)
        expected = False
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_third(self):
        result = is_increasing_or_decreasing_gradually_dampened([9,7,6,2,1], False)
        expected = False
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_fourth(self):
        result = is_increasing_or_decreasing_gradually_dampened([1,3,2,4,5], False)
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_fifth(self):
        result = is_increasing_or_decreasing_gradually_dampened([8,6,4,4,1], False)
        expected = True
        self.assertEqual(result, expected)

    def test_is_increasing_gradually_sixth(self):
        result = is_increasing_or_decreasing_gradually_dampened([1,3,6,7,9], False)
        expected = True
        self.assertEqual(result, expected)
    def test_increasing_last(self):
        result = is_increasing_or_decreasing_gradually_dampened([76,79,80,83,85,86,88], False)
        expeced = True
        self.assertEqual(result,expeced)

    def test_increasing_remove_first(self):
        result = is_increasing_or_decreasing_gradually_dampened([55,52,53,54,56,57], False)
        expeced = True
        self.assertEqual(result,expeced)

    def test_decreasing_remove_first(self):
        result = is_increasing_or_decreasing_gradually_dampened([52,53,52,51,50], False)
        expeced = True
        self.assertEqual(result,expeced)
    def test_red_nosed_reports_first(self):
        result = find_safe_reports([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]])
        expected = 4
        self.assertEqual(result,expected)