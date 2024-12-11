import unittest
from bridge_repair import make_operation_combinations
from bridge_repair import check_achieves_test_value
from bridge_repair import do_operation
from bridge_repair import get_total_for_possible_operations

class BrideRepairTestCase(unittest.TestCase):
    def test_make_operation_combinations_3(self):
        result = make_operation_combinations(3)
        expected = [['+', '+', '+'], ['+', '+', '*'], ['+', '+', '||'],
                    ['+', '*', '+'], ['+', '*', '*'], ['+', '*', '||'],
                    ['+', '||', '+'], ['+', '||', '*'], ['+', '||', '||'],
                    ['*', '+', '+'], ['*', '+', '*'], ['*', '+', '||'],
                    ['*', '*', '+'], ['*', '*', '*'], ['*', '*', '||'],
                    ['*', '||', '+'], ['*', '||', '*'], ['*', '||', '||'],
                    ['||', '+', '+'], ['||', '+', '*'], ['||', '+', '||'],
                    ['||', '*', '+'], ['||', '*', '*'], ['||', '*', '||'],
                    ['||', '||', '+'], ['||', '||', '*'], ['||', '||', '||']]

        self.assertEqual(result,expected)

    def test_make_operation_combinations_2(self):
        result = make_operation_combinations(2)
        expected = [['+', '+'], ['+', '*'], ['+', '||'], ['*', '+'], ['*', '*'], ['*', '||'], ['||', '+'], ['||', '*'], ['||', '||']]
        self.assertEqual(result,expected)

    def test_make_combinations_4(self):
        result = make_operation_combinations(4)
        expected = [
                    ['+', '+', '+', '+'], ['+', '+', '+', '*'], ['+', '+', '+', '||'],
                    ['+', '+', '*', '+'], ['+', '+', '*', '*'], ['+', '+', '*', '||'],
                    ['+', '+', '||', '+'], ['+', '+', '||', '*'], ['+', '+', '||', '||'],
                    ['+', '*', '+', '+'], ['+', '*', '+', '*'], ['+', '*', '+', '||'],
                    ['+', '*', '*', '+'], ['+', '*', '*', '*'], ['+', '*', '*', '||'],
                    ['+', '*', '||', '+'], ['+', '*', '||', '*'], ['+', '*', '||', '||'],
                    ['+', '||', '+', '+'], ['+', '||', '+', '*'], ['+', '||', '+', '||'],
                    ['+', '||', '*', '+'], ['+', '||', '*', '*'], ['+', '||', '*', '||'],
                    ['+', '||', '||', '+'], ['+', '||', '||', '*'], ['+', '||', '||', '||'],
                    ['*', '+', '+', '+'], ['*', '+', '+', '*'], ['*', '+', '+', '||'],
                    ['*', '+', '*', '+'], ['*', '+', '*', '*'], ['*', '+', '*', '||'],
                    ['*', '+', '||', '+'], ['*', '+', '||', '*'], ['*', '+', '||', '||'],
                    ['*', '*', '+', '+'], ['*', '*', '+', '*'], ['*', '*', '+', '||'],
                    ['*', '*', '*', '+'], ['*', '*', '*', '*'], ['*', '*', '*', '||'],
                    ['*', '*', '||', '+'], ['*', '*', '||', '*'], ['*', '*', '||', '||'],
                    ['*', '||', '+', '+'], ['*', '||', '+', '*'], ['*', '||', '+', '||'],
                    ['*', '||', '*', '+'], ['*', '||', '*', '*'], ['*', '||', '*', '||'],
                    ['*', '||', '||', '+'], ['*', '||', '||', '*'], ['*', '||', '||', '||'],
                    ['||', '+', '+', '+'], ['||', '+', '+', '*'], ['||', '+', '+', '||'],
                    ['||', '+', '*', '+'], ['||', '+', '*', '*'], ['||', '+', '*', '||'],
                    ['||', '+', '||', '+'], ['||', '+', '||', '*'], ['||', '+', '||', '||'],
                    ['||', '*', '+', '+'], ['||', '*', '+', '*'], ['||', '*', '+', '||'],
                    ['||', '*', '*', '+'], ['||', '*', '*', '*'], ['||', '*', '*', '||'],
                    ['||', '*', '||', '+'], ['||', '*', '||', '*'], ['||', '*', '||', '||'],
                    ['||', '||', '+', '+'], ['||', '||', '+', '*'], ['||', '||', '+', '||'],
                    ['||', '||', '*', '+'], ['||', '||', '*', '*'], ['||', '||', '*', '||'],
                    ['||', '||', '||', '+'], ['||', '||', '||', '*'], ['||', '||', '||', '||']
                ]

        self.assertEqual(result, expected)

    def test_do_operation(self):
        result = do_operation("*", 10, 19)
        expected = 190
        self.assertEqual(result, expected)
    def test_do_operation_156(self):
        result = do_operation("||", 15, 6)
        expected = 156
        self.assertEqual(result, expected)

    def test_do_operation_156(self):
        result = do_operation("||", 15, 6)
        expected = 156
        self.assertEqual(result, expected)

    def test_check_achieves_test_values(self):
        result = check_achieves_test_value(190, [10, 19])
        expected = True
        self.assertEqual(result,expected)

    def test_check_achieves_test_values_2(self):
        result = check_achieves_test_value(83, [17, 5])
        expected = False
        self.assertEqual(result,expected)
    def test_check_achieves_test_values_3(self):
        result = check_achieves_test_value(3267, [81, 40, 27],)
        expected = True
        self.assertEqual(result,expected)
    def test_check_achieves_test_values_7290(self):
        result = check_achieves_test_value(7290, [6, 8, 6, 15])
        expected = True
        self.assertEqual(result,expected)

    def test_check_achieves_test_value_large(self):
        result = check_achieves_test_value(478524813922, [9,202, 4, 13, 8, 5, 1, 1, 2, 9, 22])
        expected = True
        self.assertEqual(result, expected)

    def test_do_possible_operation(self):
        input = {
            190: [10, 19],
            3267: [81, 40, 27],
            83: [17, 5],
            156: [15, 6],
            7290: [6, 8, 6, 15],
            161011: [16, 10, 13],
            192: [17, 8, 14],
            21037: [9, 7, 18, 13],
            292: [11, 6, 16, 20]
            }
        result = get_total_for_possible_operations(input)
        expected = 11387
        self.assertEqual(result, expected)

    
