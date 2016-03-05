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
        pass

    # Test unique chars function
    def test_check_unique_chars(self):
        '''
        Ensure check_unique_chars() is returning right results
        '''

        # Import packages
        from pytools.arrays_strings.strings import check_unique_chars

        # Init variables
        unique_str = 'abcdef'
        unique_str_case = 'AaBbCc'
        non_unique_str = 'abcab'
        non_unique_str2 = 'a 2 cC.'

        # Assert unique_str
        is_unique = check_unique_chars(unique_str)
        err_msg = 'String %s is unique, should be True!'
        self.assertTrue(is_unique, msg=err_msg % unique_str)

        # Assert unique_str
        is_unique = check_unique_chars(unique_str_case)
        self.assertTrue(is_unique, msg=err_msg % unique_str_case)

        # Assert unique_str
        is_unique = check_unique_chars(unique_str)
        err_msg = 'String %s is not unique, should be False!'
        self.assertTrue(is_unique, msg=err_msg % non_unique_str)

        # Assert unique_str
        is_unique = check_unique_chars(unique_str)
        self.assertTrue(is_unique, msg=err_msg % non_unique_str2)



if __name__ == '__main__':
    unittest.main()