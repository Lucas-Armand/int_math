import unittest

import sys
sys.path.insert(1, '../')

import int_math


class TestMethods(unittest.TestCase):

    def test_modular_multiplicative_inverse_example(self):
        self.assertEqual(int_math.mod_inv(3, 26), 9)

    def test_modular_multiplicative_inverse_error(self):
        with self.assertRaises(Exception):
            int_math.mod_inv(3, 3)

if __name__ == '__main__':
    unittest.main()
