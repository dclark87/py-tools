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
        # Key-value pair
        self.key = key
        self.value = value
        # Children and parent
        self.left_child = None
        self.right_child = None
        self.parent = None
        # Status flags
        self.is_left_child = False
        self.is_right_child = False

    def insert(self, key, value):
        '''
        Insert new key-value subtree into Tree
        '''

        # Check key is numeric
        if not (isinstance(key, int) or isinstance(key, float)):
            err_msg = 'Key: "%s" must be an integer or float!' % (str(key))
            raise KeyError(err_msg)

        # If key < current key, insert right
        if key < self.key:
            if self.left_child:
                self.left_child.insert(key, value)
            else:
                self.left_child = BinarySearchTree(key, value)
                self.left_child._set_as_left_child()
                self.left_child.parent = self
        # If key > current key, insert right
        elif key > self.key:
            if self.right_child:
                self.right_child.insert(key, value)
            else:
                self.right_child = BinarySearchTree(key, value)
                self.right_child._set_as_right_child()
                self.right_child.parent = self
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
            return self

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

    def _replace_node_data(self, key, value, left_child, right_child):
        '''
        Replace the node data and connections
        '''
        # Populate key and value
        self.key = key
        self.value = value

        # Populate children
        self.left_child = left_child
        self.right_child = right_child

        # Populate children parent fields
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def _set_as_right_child(self):
        '''
        Function to make it easier to set/unset right child status
        '''
        self.is_right_child = True
        self.is_left_child = False

    def _set_as_left_child(self):
        '''
        Function to make it easier to set/unset left child status
        '''
        self.is_left_child = True
        self.is_right_child = False

    def delete(self, key):
        '''
        Delete subtree with specified key
        '''

        # First find subtree node
        curr_node = self.retrieve(key)
        if not curr_node:
            err_msg = 'Node with key: %s not found; cannot delete!' % str(key)
            raise KeyError(err_msg)

        # If leaf, assign parent pointer (left or right) to None
        if not (curr_node.left_child or curr_node.right_child):
            # If it's not the root node
            if curr_node.parent:
                if curr_node == curr_node.parent.left_child:
                    curr_node.parent.left_child = None
                else:
                    curr_node.parent.right_child = None
            # Else it is the root node, set to None
            else:
                curr_node._replace_node_data(key=None, value=None,
                                             left_child=None, right_child=None)
        # Has a left child only
        elif curr_node.left_child and not curr_node.right_child:
            # If it is a left child, put its left child as parent's left
            if curr_node.is_left_child:
                curr_node.parent.left_child = curr_node.left_child
                curr_node.left_child.parent = curr_node.parent
            # Else it is a right child, put its left child as parent's right
            elif curr_node.is_right_child:
                curr_node.parent.right_child = curr_node.left_child
                curr_node.left_child.parent = curr_node.parent
            # Else it is the root node, replace key, value, and children
            else:
                curr_node._replace_node_data(key=curr_node.left_child.key,
                                             value=curr_node.left_child.value,
                                             left_child=curr_node.left_child,
                                             right_child=None)
        # Has right child only
        elif curr_node.right_child and not curr_node.left_child:
            # If it is a left child, put its right child as parent's left
            if curr_node.is_left_child:
                curr_node.parent.left_child = curr_node.right_child
                curr_node.right_child.parent = curr_node.parent
            # Else it is a right, put its right child as parent's right
            elif curr_node.is_right_child:
                curr_node.parent.right_child = curr_node.right_child
                curr_node.right_child.parent = curr_node.parent
            # Else it is the root node, replace key, value, and children
            else:
                curr_node._replace_node_data(key=curr_node.right_child.key,
                                             value=curr_node.right_child.value,
                                             left_child=None,
                                             right_child=curr_node.right_child)
        # Else, has both left and right child, find successor
        else:
            # Get the next largest node (left leaf node in right subtree)
            successor = curr_node.right_child
            while successor.left_child:
                successor = successor.left_child
            # Check if it has a right child (it wont ever have a left)
            if successor.right_child:
                # Set its right child's parent to its parent
                successor.right_child.parent = successor.parent
                # If it's a left child, set parent's left to its right
                if successor.is_left_child:
                    successor.parent.left_child = successor.right_child
                # Else it must be a right child, set parents right to its right
                else:
                    successor.parent.right_child = successor.right_child
            # Else, it has no children, set parent's left child to None
            else:
                if successor.is_left_child:
                    successor.parent.left_child = None
                else:
                    successor.parent.right_child = None
            # Replace node data of curr_node with successor data
            curr_node.key = successor.key
            curr_node.value = successor.value

    def __iter__(self):
        '''
        Allow iteration over BST, is ran recursively via for loop
        '''

        # If child exists
        if self:
            # Do left all-way down
            if self.left_child:
                # Recursion here (__iter__ overrides for)
                for elem in self.left_child:
                    yield elem
            # Yield key value
            yield self.key
            # Then do right all-way down
            if self.right_child:
                # Recursion here (__iter__ overrides for)
                for elem in self.right_child:
                    yield elem


class BinaryHeap(object):
    '''
    Binary Heap class - priority queue implementation (min heap);
    enqueue and dequeue items in O(logn) time 
    '''

    def __init__(self):
        '''
        Init the binary heap
        '''
        self.heap_list = [0]
        self.current_size = 0

    def _get_min_child(self, idx):
        '''
        Method used to find index of minimum child of a node
        '''

        # If the right child node does not exist, return left
        if idx*2 + 1 > self.current_size:
            return idx*2
        # Get left and right children indexs
        left = idx*2
        right = idx*2+1
        # If left key is smaller, return left
        if self.heap_list[left] < self.heap_list[right]:
            return left
        # Else return right
        else:
            return right

    def _percolate_up(self, idx):
        '''
        Method to send new input key to as far to top of tree heap
        while maintaining parent-child property
        '''

        # While parent is not root
        while idx//2 > 0:
            # If the last added node is smaller than parent
            if self.heap_list[idx] < self.heap_list[idx//2]:
                # Swap parent and child
                tmp = self.heap_list[idx//2]
                self.heap_list[idx//2] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            # Check next parent/child combo if a swap is needed
            idx = idx//2

    def _percolate_down(self, idx):
        '''
        Method to send shifted root key as far down tree heap while
        maintaining parent-child property
        '''

        # While index is not a leaf
        while idx*2 <= self.current_size:
            # Get the minimum child idx
            min_child_idx = self._get_min_child(idx)
            # If the parent is greater than minimum child
            if self.heap_list[idx] > self.heap_list[min_child_idx]:
                # Swap parent and min child
                tmp = self.heap_list[min_child_idx]
                self.heap_list[min_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            # Check next parent/child combo if a swap is needed
            idx = min_child_idx

    def insert(self, key):
        '''
        Insert a new node into the BinaryHeap tree
        '''

        # Append key to end of list
        self.heap_list.append(key)
        # Increase size of heap
        self.current_size += 1
        # Percolate it up until heap order property is satisfied
        self._percolate_up(self.current_size)

    def dequeue_min(self):
        '''
        Method to return the smallest key item in the heap
        '''

        # Smallest key node is always heap[1]
        min_key = self.heap_list[1]

        # Pop latest value off end and enter as root
        # This keeps heap structure property
        self.heap_list[1] = self.heap_list[self.current_size]
        # Decrement size and pop off value
        self.current_size -= 1
        self.heap_list.pop()
        # Percolate the new root back down
        self._percolate_down(1)

        # Return the minimum key
        return min_key

    def build_heap(self, in_list):
        '''
        Build a heap tree from an unsorted input list
        '''

        # Set heap to [0, ...(in_list)] and set size
        self.heap_list = [0] + in_list
        self.current_size = len(in_list)
        # Start percolating down from parents of leaves
        # Since it is a complete tree, len//2 as a start guarantees
        # Percolating from right-to-left, bottom-to-top via idx-=1
        idx = self.current_size//2
        while idx > 0:
            # Percolate parent level down
            self._percolate_down(idx)
            # Move idx base up and repeat downward percolation of rest
            idx -= 1


class AVLBinaryTree(BinarySearchTree):
    '''
    The AVL balanced BinarySearchTree class
    '''

    def __init__(self, key, value):
        '''
        Init AVL BST via BST class init and balance factor
        '''
        super(AVLBinaryTree, self).__init__(key, value)
        self.balance_factor = 0

    def _rotate_left(self):
        '''
        Rotate a subtree (self is subtree root) left to balance out
        when subtree is right-heavy (balance_factor > 1)
        '''

        # Init new and old roots
        old_root = self
        new_root = self.right_child
        # Set old root right child (even if new root's left is None)
        old_root.right_child = new_root.left_child
        # If the old root received right child
        if old_root.right_child:
            # Set right as right child
            old_root.right_child._set_as_right_child()
            # Set right parent as old root
            old_root.right_child.parent = old_root

        # Associate old root's parent's left/right child attribute
        # to new root
        if old_root.is_left_child:
            old_root.parent.left_child = new_root
        elif old_root.is_right_child:
            old_root.parent.right_child = new_root
        # Set new root's parent to old root's parent
        new_root.parent = old_root.parent
        # And set old root to be left child or new root
        new_root.left_child = old_root
        old_root._set_as_left_child()
        old_root.parent = new_root

        # Update balance factors of new and old roots
        # Proof at: http://bit.ly/1UEmUe3
        old_root.balance_factor = old_root.balance_factor + 1 - \
                                  min(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor + 1 + \
                                  max(0, old_root.balance_factor)

    def _rotate_right(self):
        '''
        Rotate a subtree (self is subtree root) right to balance out
        when subtree is left-heavy (balance_factor < 1)
        '''
        # Init new and old root
        old_root = self
        new_root = self.left_child
        # Set old root left child (even if new root's right is None)
        old_root.left_child = new_root.right_child
        if new_root.right_child:
            old_root.left_child._set_as_left_child()
            old_root.left_child.parent = old_root

        # Associate old root's parent's left/right child attribute
        # to new root
        if old_root.is_left_child:
            old_root.parent.left_child = new_root
        elif old_root.is_right_child:
            old_root.parent.right_child = new_root
        # Set new roots parent to old root's parent
        new_root.parent = old_root.parent
        # And set old root to be right child or new root
        new_root.right_child = old_root
        old_root._set_as_right_child()
        old_root.parent = new_root

        # Update balance factors of new and old roots
        # Proof at: http://bit.ly/1UEmUe3
        old_root.balance_factor = old_root.balance_factor - 1 - \
                                  max(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor - 1 + \
                                  min(0, old_root.balance_factor)

    def _rebalance(self):
        '''
        Method to re-balance the subtree based on balance factor
        of top root node passed in (self)
        '''

        # If top root is right-heavy
        if self.balance_factor < 0:
            # If right child is left-heavy
            if self.right_child.balance_factor > 0:
                # Rotate right around right child
                self.right_child._rotate_right()
            # Rotate left around top root
            self._rotate_left()
        # If top root is left-heavy
        elif self.balance_factor > 0:
            # If left child is right-heavy
            if self.left_child.balance_factor < 0:
                # Rotate left around left child
                self.left_child._rotate_left()
            # Rotate right around top root
            self.rotate_right()

    def _update_balance(self):
        '''
        Method to check and update balance and balance factor of a
        node and its parents if necessary
        '''

        # Check if current node is out of balance limits
        if abs(self.balance_factor) > 1:
            self._rebalance()
            return
        # Otherwise, if the parent exists, update it and check it
        elif self.parent != None:
            if self.is_left_child:
                self.parent.balance_factor += 1
            elif self.is_right_child:
                self.parent.balance_factor -= 1
            # If parent becomes unbalanced
            if self.parent.balance_factor != 0:
                # Update and re-balance its parent if necessary
                self.parent._update_balance()

    def insert(self, key, value):
        '''
        Insert a new key-value subtree into BST
        '''

        # Check key is numeric
        if not isinstance(key, int) or isinstance(key, float):
            err_msg = 'Key: "%s" must be an integer or float!' % (str(key))
            raise KeyError(err_msg)

        # If key < self.key, insert left
        if key < self.key:
            # If left child exists already, recursively call
            if self.left_child:
                self.left_child.insert(key, value)
            # Otherwise, insert new left child
            else:
                self.left_child = AVLBinaryTree(key, value)
                self.left_child._set_as_left_child()
                self.left_child.parent = self
                # Update self (left child's parent) balance
                self._update_balance()
        # If key > current key, insert right
        elif key > self.key:
            # If right child exists already, recursively call
            if self.right_child:
                self.right_child.insert(key, value)
            # Otherwise, insert new right child
            else:
                self.right_child = AVLBinaryTree(key, value)
                self.right_child._set_as_right_child()
                self.right_child.parent = self
                # Update self (right child's parent) balance
                self._update_balance()
        # Key == current key, replace
        else:
            self.value = value
