# test/unit/recursion/power_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/parentheses module
'''

# Import packages
import math
import unittest

from pytools.recursion import power

class PowerTestCase(unittest.TestCase):
    '''
    Test case for power function
    '''

    def test_power(self):
        base = 2.7
        exp = 3
        expected = math.pow(base, exp)
        self.assertAlmostEqual(expected, power.power(base, exp), places=6)

        base = 3.4
        exp = -4
        expected = math.pow(base, exp)
        self.assertAlmostEqual(expected, power.power(base, exp), places=6)