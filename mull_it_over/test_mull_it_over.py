import unittest
from mull_it_over import get_valid_mul_instructions
from mull_it_over import get_total_multiplication

class MullItOverTestCase(unittest.TestCase):
    def test_get_valid_instructions(self):
        result = get_valid_mul_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        expected = ["mul(2,4)","mul(8,5)"]
        self.assertEqual(result, expected)
    def test_do_multiplication(self):
        result = get_total_multiplication(["mul(2,4)", "mul(5,5)","mul(11,8)","mul(8,5)"])
        expected = 161
        self.assertEqual(result,expected)