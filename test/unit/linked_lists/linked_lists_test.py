# test/unit/linked_lists/linked_lists_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on linked_lists module
'''

# Import packages
import unittest

from pytools.linked_lists import linked_lists


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
        # Populate
        # a: 1->3->5->6->None
        a_head = linked_lists.LinkedList()
        a_head.insert(6)
        a_head.insert(5)
        a_head.insert(3)
        a_head.insert(1)

        # b: 2->4->7->None
        b_head = linked_lists.LinkedList()
        b_head.insert(7)
        b_head.insert(4)
        b_head.insert(2)

        self.a_head = a_head
        self.b_head = b_head

    def test_create_insert_node(self):
        '''
        Test that a linked list can be created and populated properly via
        the insert function
        '''

        # Init variables
        linked_list = linked_lists.LinkedList()
        linked_list.insert(1)
        linked_list.insert(2)

        # Assert head of linked_list has data
        head_node = linked_list.head
        head_data = head_node.data
        err_msg = 'node_data: %d does not equal head_data: %d' \
                   % (2, head_data)
        self.assertEqual(2, head_data, msg=err_msg)

    def test_find_node(self):
        '''
        Test that the find_node function returns node of interest
        '''

        # Init variables
        linked_list = linked_lists.LinkedList()
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

        # Init variables
        linked_list = linked_lists.LinkedList()
        node_data = ['A', 'B', 'C', 'D']
        for char in node_data:
            linked_list.insert(char)

        # Reverse linked list in-place
        linked_list.reverse()

        node = linked_list.head
        for char in node_data:
            self.assertEqual(node.data, char)
            node = node.next_node

        self.assertIsNone(node)

    def test_linked_lists_equal(self):
        '''
        Tests if two linked lists are equal
        :return:
        '''

        # Import packages
        from pytools.linked_lists import linked_lists
        # Populate
        # a: 1->3->5->6->None
        a_head = linked_lists.LinkedList()
        a_head.insert(6)
        a_head.insert(5)
        a_head.insert(3)
        a_head.insert(1)

        self.assertTrue(linked_lists.linked_lists_equal(a_head.head,
                                                        self.a_head.head))

    def test_merge_sorted_lists(self):
        '''
        Test the merging of two sorted link lists into one sorted linked list
        :return:
        '''

        # Import packages
        from pytools.linked_lists import linked_lists

        # c: 1->2->3->4->5->6->7->None
        c_head = linked_lists.LinkedList()
        c_head.insert(7)
        c_head.insert(6)
        c_head.insert(5)
        c_head.insert(4)
        c_head.insert(3)
        c_head.insert(2)
        c_head.insert(1)

        merged = linked_lists.merge_sorted_lists(self.a_head.head,
                                                 self.b_head.head)

        self.assertTrue(linked_lists.linked_lists_equal(c_head.head,
                                                        merged))


if __name__ == '__main__':
    unittest.main()