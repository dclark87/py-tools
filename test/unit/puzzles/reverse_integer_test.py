# test/unit/puzzles/reverse_integer_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the reverse_integer module
'''

# Import packages
import unittest

from pytools.puzzles import reverse_integer

class ReverseIntegerTestCase(unittest.TestCase):
    '''
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_reverse_integer(self):
        '''
        Test the reverse_integer function works properly
        :return:
        '''

        int1 = 123
        int2 = 3049582
        int3 = 9999

        self.assertEqual(int(str(int1)[::-1]),
                         reverse_integer.reverse_integer(int1))
        self.assertEqual(int(str(int2)[::-1]),
                         reverse_integer.reverse_integer(int2))
        self.assertEqual(int(str(int3)[::-1]),
                         reverse_integer.reverse_integer(int3))


