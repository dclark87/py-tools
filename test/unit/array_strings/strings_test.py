# test/unit/array_strings/strings_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on strings.py
'''

# Import packages
import unittest

import pytools.arrays_strings.strings as strings

class CheckUniqueCharsTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        self.unique_str = 'abcdef'
        self.unique_str_case = 'AaBbCc'
        self.non_unique_str = 'abcab'
        self.non_unique_str2 = 'a 2 cC.'
        self.not_string = 123

    # Test unique chars function
    def test_check_unique_chars(self):
        '''
        Ensure check_unique_chars() is returning right results
        '''

        # Assert unique_str
        is_unique = strings.check_unique_chars(self.unique_str)
        err_msg = 'String %s is unique, should be True!'
        self.assertTrue(is_unique, msg=err_msg % self.unique_str)

        # Assert unique_str_case
        is_unique = strings.check_unique_chars(self.unique_str_case)
        self.assertTrue(is_unique, msg=err_msg % self.unique_str_case)

        # Assert non_unique_str
        is_unique = strings.check_unique_chars(self.non_unique_str)
        err_msg = 'String %s is not unique, should be False!'
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str)

        # Assert non_unique_str2
        is_unique = strings.check_unique_chars(self.non_unique_str2)
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str2)

        # Assert non_unique_str
        err_msg = 'Input %s is not string! Should raise exception' \
                  % (str(self.not_string))
        self.assertRaises(TypeError, strings.check_unique_chars,
                          self.not_string, msg=err_msg)

    # Test unique chars function
    def test_check_unique_chars2(self):
        '''
        Ensure check_unique_chars2() is returning right results
        '''

        # Assert unique_str
        is_unique = strings.check_unique_chars2(self.unique_str)
        err_msg = 'String %s is unique, should be True!'
        self.assertTrue(is_unique, msg=err_msg % self.unique_str)

        # Assert unique_str_case
        is_unique = strings.check_unique_chars2(self.unique_str_case)
        self.assertTrue(is_unique, msg=err_msg % self.unique_str_case)

        # Assert non_unique_str
        is_unique = strings.check_unique_chars2(self.non_unique_str)
        err_msg = 'String %s is not unique, should be False!'
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str)

        # Assert non_unique_str2
        is_unique = strings.check_unique_chars2(self.non_unique_str2)
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str2)

        # Assert non_unique_str
        err_msg = 'Input %s is not string! Should raise exception' \
                  % (str(self.not_string))
        self.assertRaises(TypeError, strings.check_unique_chars2,
                          self.not_string, msg=err_msg)


class ReverseCStyleStringTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_reverse_cstyle_str(self):
        '''
        Ensure that reverse_cstyle_str() is working properly
        '''

        # Init variables
        cstyle_str1 = 'abcd\0'
        cstyel_str1_rev = cstyle_str1[::-1]
        cstyle_str2 = 'dcbabcd\0'
        cstyel_str2_rev = cstyle_str2[::-1]

        # Assert cstyle str1 is reversed
        rev_str1 = strings.reverse_cstyle_str(cstyle_str1)
        err_msg = '%s is not reversed version of %s' % (rev_str1, cstyel_str1_rev)
        self.assertEqual(cstyel_str1_rev, rev_str1, msg=err_msg)

        # Assert cstyle str1 is reversed
        rev_str2 = strings.reverse_cstyle_str(cstyle_str2)
        err_msg = '%s is not reversed version of %s' % (rev_str2, cstyel_str2_rev)
        self.assertEqual(cstyel_str2_rev, rev_str2, msg=err_msg)


class RemoveDupCharsTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        self.dup_str1 = 'aZzqrsqtss'
        self.dup_str1_unique = ''.join(sorted(set(self.dup_str1),
                                              key=self.dup_str1.index))
        self.dup_str2 = 'abababababa'
        self.dup_str2_unique = ''.join(sorted(set(self.dup_str2),
                                              key=self.dup_str2.index))
        self.dup_str3 = 'aZaa'
        self.dup_str3_unique = ''.join(sorted(set(self.dup_str3),
                                              key=self.dup_str3.index))

    def test_remove_dup_chars(self):
        '''
        Ensure that remove_dup_chars() is working properly
        '''

        # Test against inputs
        non_dup_str1 = strings.remove_dup_chars(self.dup_str1)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str1, self.dup_str1)
        self.assertEqual(self.dup_str1_unique, non_dup_str1, msg=err_msg)

        non_dup_str2 = strings.remove_dup_chars(self.dup_str2)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str2, self.dup_str2)
        self.assertEqual(self.dup_str2_unique, non_dup_str2, msg=err_msg)

        non_dup_str3 = strings.remove_dup_chars(self.dup_str3)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str3, self.dup_str3)
        self.assertEqual(self.dup_str3_unique, non_dup_str3, msg=err_msg)

    def test_remove_dup_chars2(self):
        '''
        Ensure that remove_dup_chars2() is working properly
        '''

        # Test against inputs
        non_dup_str1 = strings.remove_dup_chars2(self.dup_str1)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str1, self.dup_str1)
        self.assertEqual(self.dup_str1_unique, non_dup_str1, msg=err_msg)

        non_dup_str2 = strings.remove_dup_chars2(self.dup_str2)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str2, self.dup_str2)
        self.assertEqual(self.dup_str2_unique, non_dup_str2, msg=err_msg)

        non_dup_str3 = strings.remove_dup_chars2(self.dup_str3)
        err_msg = '%s did not remove duplicates from input %s' \
                  % (non_dup_str3, self.dup_str3)
        self.assertEqual(self.dup_str3_unique, non_dup_str3, msg=err_msg)


class CheckAnagramsTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        self.ana1 = 'abcdefg'
        self.ana2 = 'gfedabc'
        self.ana3 = 'wxyZ'
        self.ana4 = 'wZxy'

    def test_check_anagrams(self):
        '''
        Check the check_anagrams function is working properly
        '''

        are_anagrams1 = strings.check_anagrams(self.ana1, self.ana2)
        self.assertTrue(are_anagrams1)

        are_anagrams2 = strings.check_anagrams(self.ana3, self.ana4)
        self.assertTrue(are_anagrams2)

        arent_anagrams1 = strings.check_anagrams(self.ana1, self.ana3)
        self.assertFalse(arent_anagrams1)

        arent_anagrams2 = strings.check_anagrams(self.ana2, self.ana4)
        self.assertFalse(arent_anagrams2)


class PalindromesTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    def test_largest_palindrome(self):
        '''
        Check the find_largest_palindrome functions are working
        properly
        '''

        # Double for loop implementation
        largest = strings.find_largest_palindrome('sfracecardfa')
        self.assertEqual(largest, 'racecar')
        # While loop implementation
        largest = strings.find_largest_palindrome2('sfracecardfa')
        self.assertEqual(largest, 'racecar')


class FindPermutationsTestCase(unittest.TestCase):
    '''
    TestCase for the strings.py module
    '''

    def test_find_permutations(self):
        '''
        Test the find permutations function
        '''

        str1 = 'ab'
        out1 = set(['ab', 'ba'])
        self.assertEqual(out1, set(strings.find_permutations(str1)))

        str2 = 'abc'
        out2 = set(['abc', 'bac', 'bca', 'cab', 'cba', 'acb'])
        self.assertEqual(out2, set(strings.find_permutations(str2)))


class FindValidParenthesesTestCase(unittest.TestCase):
    '''
    Test case for the find_valid_parentheses function
    '''

    def test_find_valid_parentheses(self):
        balanced_pars = '((a+b)*(c+d))*(a*c)+(d+b)'
        unbalanced_pars = 'a*b+(c-d*(d-e)+a'

        self.assertTrue(strings.find_valid_parentheses(balanced_pars))
        self.assertFalse(strings.find_valid_parentheses(unbalanced_pars))


# Run unittests via main executable
if __name__ == '__main__':
    unittest.main()