# test/unit/graph_trees/utils_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on graph_trees/utils module
'''

# Import packages
import unittest


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
        from pytools.graphs_trees import utils

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

        # Import packages
        from pytools.graphs_trees import utils

        # Min height should be log_2(n)
        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0, len(self.sorted_arr)-1)
        tree_proper = utils.verify_tree_property(bin_tree)
        self.assertTrue(tree_proper)

    def test_llists_from_bst(self):
        '''
        Test the llists_from_bst function
        '''

        # Import packages
        from pytools.graphs_trees import trees, utils
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


if __name__ == '__main__':
    unittest.main()