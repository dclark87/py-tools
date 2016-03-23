# test/unit/graph_trees/trees_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the trees module
'''

# Import packages
import unittest


class BinaryTreeTestCase(unittest.TestCase):
    '''
    TestCase for the BinaryTree class from the trees.py module
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
        binary_tree.insert_right('e')
        # Insert f subtree
        binary_tree.insert_right(value='f', rootval='e')

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


class TrieTestCase(unittest.TestCase):
    '''
    TestCase for the Trie class from the trees.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_insert_retrieve(self):
        '''
        Test we can insert and retrieve strings into Trie properly
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init trie object
        trie = trees.Trie()

        # Insert several strings
        trie.insert('hello')
        trie.insert('howdy')
        trie.insert('panda')
        trie.insert('polarbear')
        trie.insert('polar')
        trie.insert('hell')
        trie.insert('helsinki')

        # Retrieve a few unique strings
        err_msg = 'Retrieval returned: %s, expected: %s'
        howdy = trie.retrieve('howdy')
        self.assertEqual(howdy, 'howdy', msg=err_msg % (howdy, 'howdy'))

        panda = trie.retrieve('panda')
        self.assertEqual(panda, 'panda', msg=err_msg % (panda, 'panda'))

        # Retrieve strings with only prefixes
        polarbear = trie.retrieve('polarb')
        self.assertEqual(polarbear, 'polarbear',
                         msg=err_msg % (polarbear, 'polarbear'))
 
        hell = trie.retrieve('hel')
        self.assertEqual(hell, 'hell', msg=err_msg % (hell, 'hell'))

        # Retrieve full word that is also a prefix
        hell = trie.retrieve('hell')
        self.assertEqual(hell, 'hell', msg=err_msg % (hell, 'hell'))
        # Retrieve hello too
        hello = trie.retrieve('hello')
        self.assertEqual(hello, 'hello', msg=err_msg % (hello, 'hello'))
        # Retrieve helsinki via prefix
        helsinki = trie.retrieve('hels')
        self.assertEqual(helsinki, 'helsinki', msg=err_msg % (helsinki, 'helsinki'))

        # Assert that a KeyError is raised for non-existent prefix
        self.assertRaises(KeyError, trie.retrieve, 'helb')

    def _print_contents(self):
        '''
        Print for visual inspection
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init trie object
        trie = trees.Trie()

        # Insert several strings
        trie.insert('jack')
        trie.insert('jill')
        trie.insert('dan')
        trie.insert('daniel')
        trie.insert('danielle')

        # Print contents
        trie.print_contents()


class BinarySearchTreeTestCase(unittest.TestCase):
    '''
    TestCase for the BinarySearchTree class from the trees.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        self.kv1 = (32, '32')
        self.kv2 = (12, '12')
        self.kv3 = (72, '72')
        self.kv4 = (21, '21')
        self.kv5 = (100, '100')
        self.kv6 = (3.14, 'pi')
        self.kv7 = (99, 'red balloons')
        self.kv8 = (98, '98')
        self.kv9 = (101, 'dalmations')
        self.kv10 = (25, 'cents')

    def _populate_bst(self):
        '''
        Populate the BST
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init tree and insert
        binary_search_tree = trees.BinarySearchTree(*self.kv1)
        binary_search_tree.insert(*self.kv2)
        binary_search_tree.insert(*self.kv3)
        binary_search_tree.insert(*self.kv4)
        binary_search_tree.insert(*self.kv5)
        binary_search_tree[self.kv6[0]] = self.kv6[1]
        binary_search_tree[self.kv7[0]] = self.kv7[1]
        binary_search_tree[self.kv8[0]] = self.kv8[1]
        binary_search_tree[self.kv9[0]] = self.kv9[1]
        binary_search_tree[self.kv10[0]] = self.kv10[1]

        # Return BST populated
        return binary_search_tree

    def test_insert_retrieve(self):
        '''
        Test the BST insert function
        '''

        # Populate the BST
        binary_search_tree = self._populate_bst()

        # And retrieve values
        node1 = binary_search_tree.retrieve(self.kv1[0])
        self.assertEqual(node1.value, self.kv1[1])
        node2 = binary_search_tree.retrieve(self.kv2[0])
        self.assertEqual(node2.value, self.kv2[1])
        node4 = binary_search_tree[self.kv4[0]]
        self.assertEqual(node4.value, self.kv4[1])
        node3in = self.kv3[0] in binary_search_tree
        self.assertTrue(node3in)
        node5 = binary_search_tree[self.kv5[0]]
        self.assertEqual(node5.value, self.kv5[1])

        # Try retrieving, overwrite, and retrieve again
        pi = binary_search_tree.retrieve(self.kv6[0])
        self.assertEqual(pi.value, self.kv6[1])
        binary_search_tree[self.kv6[0]] = '3.14'
        pi = binary_search_tree[self.kv6[0]]
        self.assertEqual(pi.value, '3.14')

    def test_delete(self):
        '''
        Test that a node can be deleted from the BST
        '''

        # Populate the BST
        binary_search_tree = self._populate_bst()

        # Delete leaf node
        binary_search_tree.delete(self.kv6[0])
        kv6_in_bst = self.kv6[0] in binary_search_tree
        self.assertFalse(kv6_in_bst)

        # Delete node with left child
        binary_search_tree.delete(self.kv7[0])
        kv7_in_bst = self.kv7[0] in binary_search_tree
        self.assertFalse(kv7_in_bst)
        kv8_in_bst = self.kv8[0] in binary_search_tree
        self.assertTrue(kv8_in_bst)

        # Delete node with right child
        binary_search_tree.delete(self.kv4[0])
        kv4_in_bst = self.kv4[0] in binary_search_tree
        self.assertFalse(kv4_in_bst)
        kv10_in_bst = self.kv10[0] in binary_search_tree
        self.assertTrue(kv10_in_bst)

        # Re-populate full tree for delete with both children test
        binary_search_tree = self._populate_bst()

        # Delete left child with both children
        binary_search_tree.delete(self.kv2[0])
        kv2_in_bst = self.kv2[0] in binary_search_tree
        self.assertFalse(kv2_in_bst)
        kv4_in_bst = self.kv4[0] in binary_search_tree
        self.assertTrue(kv4_in_bst)
        kv6_in_bst = self.kv4[0] in binary_search_tree
        self.assertTrue(kv4_in_bst)
        kv10_in_bst = self.kv10[0] in binary_search_tree
        self.assertTrue(kv10_in_bst)

        # Delete right child with both children
        binary_search_tree.delete(self.kv5[0])
        kv5_in_bst = self.kv5[0] in binary_search_tree
        self.assertFalse(kv5_in_bst)
        kv7_in_bst = self.kv7[0] in binary_search_tree
        self.assertTrue(kv7_in_bst)
        kv8_in_bst = self.kv8[0] in binary_search_tree
        self.assertTrue(kv8_in_bst)
        kv9_in_bst = self.kv9[0] in binary_search_tree
        self.assertTrue(kv9_in_bst)

    def test_iterator(self):
        '''
        Test the BST can be iterated over and returns elements in order
        '''

        # Init BST
        binary_search_tree = self._populate_bst()

        # Check elements are in ascending order
        keys = [key for key in binary_search_tree]
        self.assertEqual(keys, sorted(keys))


class BinaryHeapTestCase(unittest.TestCase):
    '''
    TestCase for the BinaryHeap class from the trees.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_insert_dequeue(self):
        '''
        Test whether tree is populated correctly via insert
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init variables
        in_keys = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

        # Init heap and insert
        binary_heap = trees.BinaryHeap()
        for key in in_keys:
            binary_heap.insert(key)
        # Make sure all items are in
        self.assertEqual(len(in_keys), binary_heap.current_size)

        # Sort in keys and compare with dequeued list
        sorted_in = sorted(in_keys)
        dequeued_out = []
        for idx in range(len(in_keys)):
            dequeued_out.append(binary_heap.dequeue_min())

        self.assertEqual(dequeued_out, sorted_in)


if __name__ == '__main__':
    unittest.main()