# test/unit/puzzles/bst_to_llist_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on puzzles/bst_to_llist module
'''

# Import packages
import unittest

from pytools.puzzles.bst_to_llist import bst_to_llist
from pytools.graphs_trees.trees import BinarySearchTree


class BstToLlistTestCase(unittest.TestCase):
    '''
    Test case for the bst_to_llist module
    '''

    def test_bst_to_llist(self):
        '''
        Test to ensure that the doubly-linked list is formed (circular) and
        sorted

        :return:
        '''

        slist = [1, 2, 3, 4, 5, 6, 7]

        bst = BinarySearchTree(slist[0], slist[0])
        for i in xrange(2, len(slist)+1):
            bst.insert(i, i)

        head = bst_to_llist(bst)
        node = head
        i = 0
        while i < len(slist):
            self.assertEqual(node.value, slist[i])
            node = node._next
            i += 1