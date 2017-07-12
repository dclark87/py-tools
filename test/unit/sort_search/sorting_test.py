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
        Test the merge sort function is working properly
        '''

        # Import packages
        from pytools.sort_search import sorting

        input_arr = [4, 6, 3, 9.5, 0, 12, -1]
        sorted_arr = sorted(input_arr)
        merge_sorted = sorting.merge_sort(input_arr)

        self.assertEqual(sorted_arr, merge_sorted)

    def test_quick_sort(self):
        '''
        Test the quick sort function is working properly
        '''
 
        # Import packages
        from pytools.sort_search import sorting
 
        input_arr = [4, 6, 3, 9.5, 0, 12, -1]
        sorted_arr = sorted(input_arr)
        quick_sorted = sorting.quick_sort(input_arr)
 
        self.assertEqual(sorted_arr, quick_sorted)

    def test_insertion_sort_end(self):
        '''
        Test the insertion sort with new element at end is working properly
        '''

        # Import packages
        from pytools.sort_search import sorting

        input_arr1 = [2, 3, 4, 6, 7, 9, 0]
        input_arr2 = [2, 3, 8, 9, 12, 6]

        self.assertEqual(sorting.insertion_sort_end(input_arr1),
                         sorted(input_arr1))
        self.assertEqual(sorting.insertion_sort_end(input_arr2),
                         sorted(input_arr2))

    def test_insertion_sort(self):
        '''
        Test the insertion sort with new element at end is working properly
        '''

        # Import packages
        from pytools.sort_search import sorting

        input_arr1 = [2, 9, 4, 0, 7, 9, 0]
        input_arr2 = [2, 3, 34, 24, 12, 6]

        self.assertEqual(sorting.insertion_sort(input_arr1),
                         sorted(input_arr1))
        self.assertEqual(sorting.insertion_sort(input_arr2),
                         sorted(input_arr2))


if __name__ == '__main__':
    unittest.main()