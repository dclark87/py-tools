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
        pass

    def test_insert_retrieve(self):
        '''
        Test the BST insert function
        '''

        # Import packages
        from pytools.graphs_trees import trees

        # Init variables
        kv1 = (32, '32')
        kv2 = (12, '12')
        kv3 = (72, '72')
        kv4 = (21, '21')
        kv5 = (100, '100')
        kv6 = (3.14, 'pi')

        # Init tree and insert
        binary_search_tree = trees.BinarySearchTree(*kv1)
        binary_search_tree.insert(*kv2)
        binary_search_tree.insert(*kv3)
        binary_search_tree.insert(*kv4)
        binary_search_tree.insert(*kv5)
        binary_search_tree[kv6[0]] = kv6[1]

        # And retrieve values
        val1 = binary_search_tree.retrieve(kv1[0])
        self.assertEqual(val1, kv1[1])
        val2 = binary_search_tree.retrieve(kv2[0])
        self.assertEqual(val2, kv2[1])
        val4 = binary_search_tree[kv4[0]]
        self.assertEqual(val4, kv4[1])
        val3in = kv3[0] in binary_search_tree
        self.assertTrue(val3in)
        val5 = binary_search_tree[kv5[0]]
        self.assertEqual(val5, kv5[1])

        # Try retrieving, overwrite, and retrieve again
        pi = binary_search_tree.retrieve(kv6[0])
        self.assertEqual(pi, kv6[1])
        binary_search_tree[kv6[0]] = '3.14'
        pi = binary_search_tree[kv6[0]]
        self.assertEqual(pi, '3.14')


if __name__ == '__main__':
    unittest.main()