import unittest
from resonant_collinearlity import get_antinode_positions
from resonant_collinearlity import find_all_antenna_postions

class ResonantCollinearlityTestCase(unittest.TestCase):
    def test_get_antinode_positions(self):
        result = get_antinode_positions((3,4), (5,5), 10, 10)
        expected = {(7,6), (1,3),(9,7),(3,4),(5,5)}
        self.assertEqual(result, expected)

    def test_get_antinode_positions_2(self):
        result = get_antinode_positions((4,8), (5,5), 10, 10)
        expected = {(6,2),(4,8),(5,5)}
        self.assertEqual(result, expected)

    def test_get_antinode_positions_3(self):
        result = get_antinode_positions((3,4), (4,8), 10, 10)
        expected = {(2,0),(3,4),(4,8)}
        self.assertEqual(result, expected)
    
    def test_get_antinode_positions_4(self):
        result = get_antinode_positions((0,0),(2,2),10,10)
        expected = {(4,4),(6,6),(8,8),(0,0),(2,2)}
        self.assertEqual(result,expected)
    
    def test_find_all_antena_positions(self):
        input = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'a', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', 'a', '.'],
                ['.', '.', '.', '.', '.', 'a', '.', '.', '.', '.'],
                ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]

        result = find_all_antenna_postions(input)
        expected = {(1,3), (2,0), (6,2),(7,6),(9,7),(5,5),(3,4),(4,8)}
        self.assertEqual(result, expected)

    def test_find_all_antena_positions_2(self):
        input = [['T', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
                 ['.', '.', '.', 'T', '.', '.', '.', '.', '.', '.'],
                 ['.', 'T', '.', '.', '.', '.', '#', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                 ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]

        result = find_all_antenna_postions(input)
        print(result)
        expected = {(0,0),(2,1), (4,2),(6,3),(8,4),(1,3),(0,5),(2,6),(3,9)}
        self.assertEqual(result, expected)
