# test/unit/sort_search/hash_tables_test
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on sorting module
'''

# Import packages
import unittest


class SortingTestCase(unittest.TestCase):
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

    def test_merge_sort(self):
        '''
        '''

        # Import packages
        from pytools.sort_search import sorting

        input_arr = [4,6,3,9.5,0,12,-1]
        sorted_arr = sorted(input_arr)
        merge_sorted = sorting.merge_sort(input_arr)

        self.assertEqual(sorted_arr, merge_sorted)

    def test_quick_sort(self):
        '''
        '''

        # Import packages
        from pytools.sort_search import sorting

        input_arr = [4,6,3,9.5,0,12,-1]
        sorted_arr = sorted(input_arr)
        quick_sorted = sorting.quick_sort(input_arr)

        self.assertEqual(sorted_arr, quick_sorted)

if __name__ == '__main__':
    unittest.main()