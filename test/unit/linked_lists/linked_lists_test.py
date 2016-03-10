# test/unit/linked_lists/linked_lists_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on linked_lists.py
'''

# Import packages
import unittest


class LinkedListsTestCase(unittest.TestCase):
    '''
    TestCase for the linked_lists.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    # Test can create and insert a node
    def test_create_list_insert_node(self):
        '''
        Test that a linked list can be created and populated properly
        '''

        # Import packages
        from pytools.linked_lists.linked_lists import LinkedList

        # Init variables
        linked_list = LinkedList()
        node_data = 1
        linked_list.insert(node_data)

        # Assert head of linked_list has data
        head_node = linked_list.head
        head_data = head_node.get_data()
        err_msg = 'node_data: %d does not equal head_data: %sd' \
                   % (node_data, head_data)
        self.assertEqual(node_data, head_data, msg=err_msg)


if __name__ == '__main__':
    unittest.main()