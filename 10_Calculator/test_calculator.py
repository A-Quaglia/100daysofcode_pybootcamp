import unittest
from typing import get_args

from calculator import apply_ops, add, sub, mul, div
from calculator import ops_result

NUM_LIST = [1, 2, 3]

class TestCalculator(unittest.TestCase):

    def test_apply_ops(self):
        list_char = ['h', 'i', ' ', 'l', 'e', 'l', 'e']
        join_char = lambda a,b: a+b
        self.assertEqual(apply_ops(join_char, list_char), 'hi lele')

    def test_add(self):
        self.assertEqual(add(NUM_LIST), 6)

    def test_add_type(self):
        self.assertIsInstance(add(NUM_LIST), get_args(ops_result))

    def test_sub(self):
        self.assertEqual(sub(NUM_LIST), -4)

    def test_sub_type(self):
        self.assertIsInstance(sub(NUM_LIST), get_args(ops_result))

    def test_mul(self):
        self.assertEqual(mul(NUM_LIST), 6)

    def test_mul_type(self):
        self.assertIsInstance(mul(NUM_LIST), get_args(ops_result))

    def test_div(self):
        self.assertAlmostEqual(div(NUM_LIST), 0.16666666)

    def test_div_type(self):
        self.assertIsInstance(div(NUM_LIST), get_args(ops_result))

if __name__ == '__main__':
    unittest.main()