# test/unit/linked_lists/utils_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on linked_lists/utils module
'''

# Import packages
import unittest


class RemoveLListDupsTestCase(unittest.TestCase):
    '''
    TestCase for the utils module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Import packages
        from pytools.linked_lists import linked_lists
        llist_dups = linked_lists.LinkedList()

        # Init instance attributes
        node_data = ['A', 'B', 'C', 'C', 'D', 'E', 'D', 'F']
        for char in node_data:
            llist_dups.insert(char)

        self.llist_dups = llist_dups

    def test_remove_dups_is_unique(self):
        '''
        Function to test the remove duplicates function
        '''

        # Import packages
        from pytools.linked_lists import utils

        # Test that the dups linked list is not unique
        not_unique = utils.is_llist_unique(self.llist_dups)
        self.assertFalse(not_unique)

        # Run function to remove dups
        llist_nondups = utils.remove_dups_llist(self.llist_dups)
        # Test it returns unique
        is_unique = utils.is_llist_unique(llist_nondups)
        self.assertTrue(is_unique)

    def test_remove_dups_inplace_is_unique(self):
        '''
        Function to test the remove duplicates in-place function
        '''

        # Import packages
        from pytools.linked_lists import utils

        # Test that the dups linked list is not unique
        not_unique = utils.is_llist_unique(self.llist_dups)
        self.assertFalse(not_unique)

        # Run function to remove dups
        llist_nondups = utils.remove_dups_llist_inplace(self.llist_dups)
        # Test it returns unique
        is_unique = utils.is_llist_unique(llist_nondups)
        self.assertTrue(is_unique)


class FindNToLastTestCase(unittest.TestCase):
    '''
    TestCase for the utils module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Import packages
        from pytools.linked_lists import linked_lists
        llist = linked_lists.LinkedList()

        # Init instance attributes
        node_data = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I']
        for char in node_data:
            llist.insert(char)

        self.llist = llist

    def test_find_n_tolast(self):
        '''
        Test the find_n_tolast() function is working properly
        '''

        # Import packages
        from pytools.linked_lists import utils

        # Test function
        data = utils.find_n_tolast(self.llist, 2)
        self.assertEqual(data, 'B')

        data = utils.find_n_tolast(self.llist, 1)
        self.assertEqual(data, 'A')

        data = utils.find_n_tolast(self.llist, 8)
        self.assertEqual(data, 'I')


if __name__ == '__main__':
    unittest.main()