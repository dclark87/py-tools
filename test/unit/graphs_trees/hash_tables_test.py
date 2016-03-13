# test/unit/graph_trees/trees_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the trees module
'''

# Import packages
import unittest


class TreesTestCase(unittest.TestCase):
    '''
    TestCase for the trees module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_insert_left(self):
        '''
        Test we can insert a left child into tree
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init variables
        binary_tree = trees.BinaryTree('a')

        # Insert b subtree
        binary_tree.insert_left('b')
        # Insert c subtree
        binary_tree.insert_left(value='c', rootval='b')

        # Get the b subtree
        b_subtree = binary_tree.find_rootval('b')
        err_msg = 'subtree value: %s does not equal expected: %s' \
                  % (b_subtree.value, 'b')
        self.assertEqual(b_subtree.value, 'b', msg=err_msg)

    def test_insert_right(self):
        '''
        Test we can insert a right child into tree
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init variables
        binary_tree = trees.BinaryTree('d')

        # Insert e subtree
        binary_tree.insert_left('e')
        # Insert f subtree
        binary_tree.insert_left(value='f', rootval='e')

        # Get the e subtree
        e_subtree = binary_tree.find_rootval('e')
        err_msg = 'subtree value: %s does not equal expected: %s' \
                  % (e_subtree.value, 'e')
        self.assertEqual(e_subtree.value, 'e', msg=err_msg)

    def test_find_node(self):
        '''
        Find a tree node based on input value
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init variables
        value1 = 'a'
        value2 = 'b'
        value3 = 12

        # Init binary tree
        binary_tree = trees.BinaryTree(value1)

        # Insert left and right childs
        binary_tree.insert_left(value2, rootval=value1)
        binary_tree.insert_right(value3, rootval=value1)

        # Find each value
        found_val1 = binary_tree.find_rootval(value1).value
        found_val2 = binary_tree.find_rootval(value2).value
        found_val3 = binary_tree.find_rootval(value3).value

        # Test that each found value is correct
        err_msg = 'Found value: %s does not equal expected value: %s'
        self.assertEqual(found_val1, value1, msg=err_msg % (found_val1, value1))
        self.assertEqual(found_val2, value2, msg=err_msg % (found_val2, value2))
        self.assertEqual(found_val3, value3, msg=err_msg % (found_val3, value3))

if __name__ == '__main__':
    unittest.main()