# test/unit/recursion/parentheses_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/parentheses module
'''

# Import packages
import unittest


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

        # Import packages
        from pytools.recursion import parentheses

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


if __name__ == '__main__':
    unittest.main()