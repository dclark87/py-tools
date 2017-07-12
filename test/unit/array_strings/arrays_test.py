# test/unit/array_strings/arrays_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on arrays.py
'''

# Import packages
import unittest

from pytools.arrays_strings import arrays

class ArraysTestCase(unittest.TestCase):
    '''
    '''

    def test_flatten_list(self):
        l = [[1, 2, [3, 4]], [5, 6], 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(expected, arrays.flatten_list(l))