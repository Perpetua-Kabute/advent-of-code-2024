import unittest
from historian_hysteria import find_distance
from historian_hysteria import find_similarity_score

"""
3   4
4   3
2   5
1   3
3   9
3   3"""
class HistorianHysteriaTestCase(unittest.TestCase):
    def test_distance_first_example(self):
        result = find_distance([3,4,2,1,3,3], [4,3,5,3,9,3])
        expected = 11
        self.assertEqual(result, expected)

    def test_distance_second_example(self):
        result = find_distance([3,3], [3,3])
        expected = 0
        self.assertEqual(result, expected)

    def test_similarity_score(self):
        result = find_similarity_score([3,4,2,1,3,3], [4,3,5,3,9,3])
        expected = 31
        self.assertEqual(result, expected)