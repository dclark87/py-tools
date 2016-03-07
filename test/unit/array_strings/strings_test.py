# test/unit/array_strings/strings_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on strings.py
'''

# Import packages
import unittest


class StringsTestCase(unittest.TestCase):
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

        # Import packages
        from pytools.arrays_strings.strings import check_unique_chars

        # Assert unique_str
        is_unique = check_unique_chars(self.unique_str)
        err_msg = 'String %s is unique, should be True!'
        self.assertTrue(is_unique, msg=err_msg % self.unique_str)

        # Assert unique_str_case
        is_unique = check_unique_chars(self.unique_str_case)
        self.assertTrue(is_unique, msg=err_msg % self.unique_str_case)

        # Assert non_unique_str
        is_unique = check_unique_chars(self.non_unique_str)
        err_msg = 'String %s is not unique, should be False!'
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str)

        # Assert non_unique_str2
        is_unique = check_unique_chars(self.non_unique_str2)
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str2)

        # Assert non_unique_str
        err_msg = 'Input %s is not string! Should raise exception' \
                  % (str(self.not_string))
        self.assertRaises(TypeError, check_unique_chars, self.not_string,
                          msg=err_msg)

    # Test unique chars function
    def test_check_unique_chars2(self):
        '''
        Ensure check_unique_chars2() is returning right results
        '''

        # Import packages
        from pytools.arrays_strings.strings import check_unique_chars2

        # Assert unique_str
        is_unique = check_unique_chars2(self.unique_str)
        err_msg = 'String %s is unique, should be True!'
        self.assertTrue(is_unique, msg=err_msg % self.unique_str)

        # Assert unique_str_case
        is_unique = check_unique_chars2(self.unique_str_case)
        self.assertTrue(is_unique, msg=err_msg % self.unique_str_case)

        # Assert non_unique_str
        is_unique = check_unique_chars2(self.non_unique_str)
        err_msg = 'String %s is not unique, should be False!'
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str)

        # Assert non_unique_str2
        is_unique = check_unique_chars2(self.non_unique_str2)
        self.assertFalse(is_unique, msg=err_msg % self.non_unique_str2)

        # Assert non_unique_str
        err_msg = 'Input %s is not string! Should raise exception' \
                  % (str(self.not_string))
        self.assertRaises(TypeError, check_unique_chars2, self.not_string,
                          msg=err_msg)

    def test_reverse_cstyle_str(self):
        '''
        Ensure that reverse_cstyle_str is returning correct results
        '''

        # Import packages
        from pytools.arrays_strings.strings import reverse_cstyle_str

        # Init variables
        cstyle_str1 = 'abcd\0'
        cstyel_str1_rev = cstyle_str1[::-1]

        # Assert cstyle str1 is reversed
        rev_str1 = reverse_cstyle_str(cstyle_str1)
        err_msg = '%s is not reversed version of %s' % (rev_str1, cstyel_str1_rev)
        self.assertEqual(cstyel_str1_rev, rev_str1, msg=err_msg)

if __name__ == '__main__':
    unittest.main()