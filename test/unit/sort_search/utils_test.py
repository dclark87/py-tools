# test/unit/sort_search/utils_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on utils module
'''

# Import packages
import unittest


class AMergeBTestCase(unittest.TestCase):
    '''
    TestCase for the sorting module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_a_merge_b(self):
        '''
        Test the a_merge_b function is working properly
        '''

        # Import packages
        from pytools.sort_search import utils

        # Init variables
        a_arr = [1, 3, 5, 7, None, None, None]
        b_arr = [2, 4, 6]
        ab_sorted = [1, 2, 3, 4, 5, 6, 7]

        # Test they are equal
        ab_merged = utils.a_merge_b(a_arr, b_arr)
        self.assertEqual(ab_merged, ab_sorted)

        # Where b needs to be at beg of a
        a_arr = [2, 3, 5, 7, None, None, None]
        b_arr = [0, 1, 6]
        ab_sorted = [0, 1, 2, 3, 5, 6, 7]

        # Test they are equal
        ab_merged = utils.a_merge_b(a_arr, b_arr)
        self.assertEqual(ab_merged, ab_sorted)


class RotArrSearchTestCase(unittest.TestCase):
    '''
    TestCase for the sorting module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_rot_arr_search(self):
        '''
        Test the rot_arr_search function is working properly
        '''

        # Import packages
        from pytools.sort_search import utils

        # Init variables
        rot_arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        elem = 5

        # Run function
        pos = utils.rot_arr_search(rot_arr, elem)
        self.assertEqual(pos, rot_arr.index(elem))


if __name__ == '__main__':
    unittest.main()