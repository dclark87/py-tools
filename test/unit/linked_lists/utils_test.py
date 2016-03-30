# test/unit/linked_lists/utils_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on linked_lists/utils module
'''

# Import packages
import unittest


class LinkedListsUtilsTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()