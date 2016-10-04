# test/unit/graph_trees/utils_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on graph_trees/utils module
'''

# Import packages
import unittest

from pytools.graphs_trees import utils

class GraphTreesUtilsTestCase(unittest.TestCase):
    '''
    TestCase for the utils module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        self.sorted_arr = [-4, 0, 3, 9, 12, 21, 23, 24]

    def test_binary_tree_from_arr(self):
        '''
        Test the binary_tree_from_arr function from the
        graph_trees/utils module
        '''

        # Import packages
        import math

        # Min height should be log_2(n)
        min_height = int(math.ceil(math.log(len(self.sorted_arr), 2)))
        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0, len(self.sorted_arr)-1)
        height = utils._get_max_height(bin_tree)
        self.assertEqual(height, min_height)

    def test_verify_tree_property(self):
        '''
        Test the binary_tree_from_arr function from the
        graph_trees/utils module
        '''

        # Min height should be log_2(n)
        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0, len(self.sorted_arr)-1)
        tree_proper = utils.verify_tree_property(bin_tree)
        self.assertTrue(tree_proper)

    def test_llists_from_bst(self):
        '''
        Test the llists_from_bst function
        '''

        # Import packages
        from pytools.graphs_trees import trees
        from pytools.linked_lists import linked_lists

        # Init BST
        bst = trees.BinarySearchTree(12, 'brady')
        bst.insert(8, 'oldkobe')
        bst.insert(24, 'newkobe')
        bst.insert(21, 'kg')
        bst.insert(2, 'bigsmooth')
        bst.insert(11, 'bledsoe')
        bst.insert(87, 'gronk')

        # Init linked lists
        llist1 = linked_lists.LinkedList()
        llist1.insert('brady')

        llist2 = linked_lists.LinkedList()
        llist2.insert('oldkobe')
        llist2.insert('newkobe')

        llist3 = linked_lists.LinkedList()
        llist3.insert('kg')
        llist3.insert('gronk')
        llist3.insert('bigsmooth')
        llist3.insert('bledsoe')

        llists2 = [llist1, llist2, llist3]

        # Call function
        llists = utils.llists_from_bst(bst)

        # Verify contents
        for idx, llist in enumerate(llists):
            llist2 = llists2[idx]
            node = llist.head
            node2 = llist2.head
            while node:
                self.assertEqual(node.data, node2.data)
                node = node.next_node
                node2 = node2.next_node

    def test_pre_order_traverse(self):
        '''
        Test the pre-order traversal function
        :return:
        '''

        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0,
                                              len(self.sorted_arr)-1)
        out_str = utils.pre_order_traverse(bin_tree)
        expected = '9 0 -4 3 21 12 23 24 '
        self.assertEqual(expected, out_str)

    def test_pre_order_recursive(self):
        '''
        Test the pre-order traversal function
        :return:
        '''

        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0,
                                              len(self.sorted_arr) - 1)
        out_str = utils.pre_order_recursive(bin_tree)
        expected = '9 0 -4 3 21 12 23 24 '
        self.assertEqual(expected, out_str)

    def test_post_order_traverse(self):
        '''
        Test the pre-order traversal function
        :return:
        '''

        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0,
                                              len(self.sorted_arr) - 1)
        out_str = utils.post_order_traverse(bin_tree)
        expected = '-4 3 0 12 24 23 21 9 '
        self.assertEqual(expected, out_str)

    def test_in_order_traverse(self):
        '''
        Test the pre-order traversal function
        :return:
        '''

        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0,
                                              len(self.sorted_arr) - 1)
        out_str = utils.in_order_traverse(bin_tree)
        expected = '-4 0 3 9 12 21 23 24 '
        self.assertEqual(expected, out_str)


if __name__ == '__main__':
    unittest.main()