# pytools/graphs_trees/trees.py
#
# Author: Daniel Clark, 2016
from __builtin__ import True

'''
This module contains functions to solve problems related to graphs and
trees data structures
'''


class BinaryTree(object):
    '''
    Tree class implemented using recursion
    '''

    def __init__(self, value):
        '''
        Init binary tree
        '''
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value, rootval=None):
        '''
        Insert subtree as left child of specified rootval

        Parameters
        ----------
        value : object
            value to insert as the subtree root value
        rootval : object (optional); default=None
            if None, inserts the new subtree as the left child of the
            root of the entire tree, if specified, it searches the tree
            for the subtree whos root value = rootval and inserts there
        '''

        # Init new tree
        new_subtree = BinaryTree(value)

        # If rootval is specified, traverse tree to find rootval
        if rootval:
            curr_subtree = self.find_rootval(rootval)
            new_subtree.left_child = curr_subtree.left_child
            curr_subtree.left_child = new_subtree
        # Otherwisse, insert subtree at root left child
        else:
            if not self.left_child:
                self.left_child = new_subtree
            else:
                curr_left = self.left_child
                self.left_child = new_subtree
                new_subtree.left_child = curr_left

    def insert_right(self, value, rootval=None):
        '''
        Insert subtree as right child of specified rootval

        Parameters
        ----------
        value : object
            value to insert as the subtree root value
        rootval : object (optional); default=None
            if None, inserts the new subtree as the left child of the
            root of the entire tree, if specified, it searches the tree
            for the subtree whos root value = rootval and inserts there
        '''

        # Init new tree
        new_subtree = BinaryTree(value)

        # If rootval is specified, traverse tree to find rootval
        if rootval:
            curr_subtree = self.find_rootval(rootval)
            new_subtree.right_child = curr_subtree.right_child
            curr_subtree.right_child = new_subtree
        # Otherwisse, insert subtree at root left child
        else:
            if not self.right_child:
                self.right_child = new_subtree
            else:
                curr_right = self.right_child
                self.right_child = new_subtree
                new_subtree.right_child = curr_right

    def find_rootval(self, rootval):
        '''
        Find and return root of tree or subtree where value = rootval
        '''

        # If the returned subtree's value is expected, return
        if self.value == rootval:
            return self
        # Otherwise iterate through children recursively to check
        # all the day down to leaf nodes of tree
        else:
            children = [self.left_child, self.right_child]
            for child in children:
                if child:
                    value = child.find_rootval(rootval)
                    if value:
                        return child


class Trie(object):
    '''
    Trie tree data structure
    '''

    def __init__(self, char='', child=None, is_leaf=False):
        '''
        Init Trie structure
        '''

        # Test for valid input
        if char:
            if not (isinstance(char, str) and len(char) == 1):
                err_msg = 'Input char: %s must be a string of length 1!' % str(char)
                raise ValueError(err_msg)

        # Populate contents
        self.char = char
        if not child:
            self.children = []
        else:
            self.children = [child]
        self.is_leaf = is_leaf

    def insert(self, string):
        '''
        Insert string into Trie
        '''

        # Get first char of input string
        prefix = string[0]
        # Iterate through self.children to see if need to insert new sub-trie
        insert_child = True
        for child in self.children:
            if child.char == prefix:
                insert_child = False
                break
        # If sub-trie with char wasnt found, create and insert
        if insert_child:
            child = Trie(prefix)
            self.children.append(child)
        # If there is more of string to populate trie with, recursively call
        # insert on sub-trie
        if len(string) > 1:
            suffix = string[1:]
            child.insert(suffix)
        # If this is final char of input string, mark as a leaf node
        else:
            child.is_leaf = True

    def retrieve(self, prefix):
        '''
        Retrieve shortest matching word entry based on a prefix;
        prefix can be partial word or full word
        '''

        # Init variables
        sub_char = ''

        # Iterate through current trie's children
        for child in self.children:
            # If still parsing prefix
            if len(prefix) > 0:
                char = prefix[0]
                # As long as sub trie char matches
                if child.char == char:
                    # If the child is a lead and it's the last char of
                    # prefix, return
                    if child.is_leaf and len(prefix) == 1:
                        sub_char = child.char
                        break
                    # Otherwise keep retrieving with rest of prefix
                    else:
                        sub_char = child.retrieve(prefix[1:])
            # If we're past end of prefix and found leaf, return
            elif child.is_leaf:
                sub_char = child.char
                break
            # Else we're past end of prefix, keep retrieving
            else:
                sub_char = child.retrieve('')

        # If made it through, char in prefix couldn't find match
        if sub_char == '':
            raise KeyError('Prefix ending in: "..%s" not in Trie!' \
                           % (self.char + prefix))

        # Return current trie char + sub_chars found
        return self.char + sub_char

    def print_contents(self):
        '''
        Print Trie object for visualization
        '''

        if len(self.children) > 0:
            print '%s -> %s' \
            % (self.char, str([(ch.char, ch.is_leaf) for ch in self.children]))
        for child in self.children:
            child.print_contents()


class BinarySearchTree(object):
    '''
    Binary Search Tree class implementation where each node in the
    tree contains a key-value pair and an optional left child and
    right child. left_child.key < parent; right_child.key > parent
    '''

    def __init__(self, key, value):
        '''
        Init tree or sub-tree
        '''
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def insert(self, key, value):
        '''
        Insert new key-value subtree into Tree
        '''

        # Check key is integer
        if not (isinstance(key, int) or isinstance(key, float)):
            err_msg = 'Key: "%s" must be an integer or float!' % (str(key))
            raise KeyError(err_msg)

        # If key < current key, insert left
        if key < self.key:
            if self.left_child:
                self.left_child.insert(key, value)
            else:
                self.left_child = BinarySearchTree(key, value)
        # If key > current key, insert right
        elif key > self.key:
            if self.right_child:
                self.right_child.insert(key, value)
            else:
                self.right_child = BinarySearchTree(key, value)
        # Key == current key, replace
        else:
            self.value = value

    def __setitem__(self, key, value):
        '''
        Allow assignment via [] operator
        '''
        self.insert(key, value)

    def retrieve(self, key):
        '''
        Find tree node value using specified key
        '''

        # Check key is integer
        if not (isinstance(key, int) or isinstance(key, float)):
            err_msg = 'Key: "%s" must be an integer or float!' % (str(key))
            raise KeyError(err_msg)

        # If key < current key, check left child
        if key < self.key:
            if not self.left_child:
                return None
            else:
                return self.left_child.retrieve(key)
        # If key > current key, check right child
        elif key > self.key:
            if not self.right_child:
                return None
            else:
                return self.right_child.retrieve(key)
        # Key == current key, return value
        else:
            return self.value


    def __getitem__(self, key):
        '''
        Allow access via [] operator
        '''
        return self.retrieve(key)

    def __contains__(self, key):
        '''
        Enable the "in" operator
        '''
        if self.retrieve(key):
            return True
        else:
            return False