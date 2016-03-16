# test/unit/linked_lists/linked_lists_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on linked_lists module
'''

# Import packages
import unittest


class LinkedListsTestCase(unittest.TestCase):
    '''
    TestCase for the linked_lists module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_create_insert_node(self):
        '''
        Test that a linked list can be created and populated properly via
        the insert function
        '''

        # Import packages
        from pytools.linked_lists.linked_lists import LinkedList

        # Init variables
        linked_list = LinkedList()
        linked_list.insert(1)
        linked_list.insert(2)

        # Assert head of linked_list has data
        head_node = linked_list.head
        head_data = head_node.get_data()
        err_msg = 'node_data: %d does not equal head_data: %d' \
                   % (2, head_data)
        self.assertEqual(2, head_data, msg=err_msg)

    def test_find_node(self):
        '''
        Test that the find_node function returns node of interest
        '''

        # Import packages
        from pytools.linked_lists.linked_lists import LinkedList

        # Init variables
        linked_list = LinkedList()
        linked_list.insert('a')
        linked_list.insert('b')
        linked_list.insert('c')
        linked_list.insert('a')

        # Find node
        a_node = linked_list.find_node('a')
        self.assertEqual(a_node.data, 'a',
                         msg='Found node: %s does not equal "a"' % a_node.data)
        c_node = linked_list.find_node('c')
        self.assertEqual(c_node.data, 'c',
                         msg='Found node: %s does not equal "c"' % c_node.data)

    def test_reverse(self):
        '''
        Test the list can be reversed in-place
        '''

        # Import packages
        from pytools.linked_lists.linked_lists import LinkedList

        # Init variables
        linked_list = LinkedList()
        node_data = ['A', 'B', 'C', 'D']
        for char in node_data:
            linked_list.insert(char)

        # Reverse linked list in-place
        linked_list.reverse()

        node = linked_list.head
        for char in node_data:
            self.assertEqual(node.data, char)
            node = node.get_next()

        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()