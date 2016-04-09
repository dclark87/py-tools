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

if __name__ == '__main__':
    unittest.main()