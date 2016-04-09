# test/unit/recursion/str_perms_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/str_perms module
'''

# Import packages
import unittest


class StrPermsTestCase(unittest.TestCase):
    '''
    TestCase for the str_perms function
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def _calc_num_perms(self, str_length):
        '''
        Function to calculate the number of permutations there should
        be given a string length
        '''

        # Import packages
        import math

        # n! is the number of perms
        return math.factorial(str_length)

    def test_str_perms(self):
        '''
        Test the permutations are correct
        '''

        # Import packages
        from pytools.recursion import str_perms

        # Init variables
        str1 = 'abc'
        perms1 = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        str_perms1 = str_perms.permutations(str1)
        self.assertEqual(sorted(str_perms1), sorted(perms1))

        str2 = 'abcd'
        perms2 = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd',
                  'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb',
                  'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac',
                  'dbca', 'dcab', 'dcba']
        str_perms2 = str_perms.permutations(str2)
        self.assertEqual(sorted(str_perms2), sorted(perms2))


if __name__ == '__main__':
    unittest.main()