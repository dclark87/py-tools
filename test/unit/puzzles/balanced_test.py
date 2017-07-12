# test/unit/puzzles/balanced_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the balanced module
'''

# Import packages
import unittest

from pytools.puzzles import balanced

class BalancedTestCase(unittest.TestCase):
    '''
    TestCase for the balanced.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_is_balanced(self):
        '''

        :return:
        '''

        # Init variables
        s1 = 'saf[df]a'
        s2 = '[[[[{{{[(('
        s3 = '()()()[][][]{}{}'
        s4 = '[dasf({[a]})((f))]'
        s5 = '([[[]]{}'

        # Run assertion tests
        self.assertTrue(balanced.is_balanced(s1))
        self.assertFalse(balanced.is_balanced(s2))
        self.assertTrue(balanced.is_balanced(s3))
        self.assertTrue(balanced.is_balanced(s4))
        self.assertFalse(balanced.is_balanced(s5))