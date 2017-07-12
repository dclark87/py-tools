# test/unit/recursion/parentheses_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/parentheses module
'''

# Import packages
import unittest

from pytools.recursion import parentheses

class ParenthPairsTestCase(unittest.TestCase):
    '''
    TestCase for the parenth_pairs function
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def test_parenth_pairs(self):
        '''
        Test the parenth_pairs() function is working properly
        '''

        # Run function and test outputs
        one_pair = parentheses.parenth_pairs(1)
        one_pair_sets = ['()']
        for pair in one_pair:
            print(pair)
            self.assertIn(pair, one_pair_sets)
        two_pair = parentheses.parenth_pairs(2)
        two_pair_sets = ['()()', '(())']
        for pair in two_pair:
            print(pair)
            self.assertIn(pair, two_pair_sets)
        three_pair = parentheses.parenth_pairs(3)
        three_pair_sets = ['((()))', '()(())', '(())()', '()()()', '(()())']
        for pair in three_pair:
            print(pair)
            self.assertIn(pair, three_pair_sets)

    def test_balanced(self):
        '''
        Test we can get all permutations of balanced parentheses

        :return:
        '''

        out2 = parentheses.return_balanced(2)
        self.assertIn('(())', out2)
        self.assertIn('()()', out2)
        out3 = parentheses.return_balanced(3)
        self.assertIn('((()))', out3)
        self.assertIn('()(())', out3)
        self.assertIn('()()()', out3)
        self.assertIn('(())()', out3)
        self.assertIn('(()())', out3)


if __name__ == '__main__':
    unittest.main()
