# test/unit/puzzles/two_trees_leaves_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on puzzles/two_trees_leaves module
'''

# Import packages
import unittest

from pytools.puzzles import two_trees_leaves
from pytools.graphs_trees import utils


class TwoTreesLeavesTestCase(unittest.TestCase):
    '''
    TestCase for the two_trees_leaves module
    '''

    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        self.sorted_arr = [-4, 0, 3, 9, 12, 21, 23, 24]
        self.sorted_arr2 = [-4, 0, 3, 9, 11, 21, 23, 24]

    def test_first_pair_nonmatch(self):
        '''
        Test the first_pair_nonmatch function

        :return:
        '''

        bin_tree = utils.binary_tree_from_arr(self.sorted_arr, 0,
                                              len(self.sorted_arr) - 1)
        bin_tree2 = utils.binary_tree_from_arr(self.sorted_arr2, 0,
                                               len(self.sorted_arr) - 1)

        nonmatch = two_trees_leaves.first_pair_nonmatch(bin_tree, bin_tree2)

        self.assertEqual((12, 11), nonmatch)
