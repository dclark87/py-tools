# pytools/graphs_trees/utils.py
#
# Author: Daniel Clark, 2016
from __builtin__ import True

'''
This module contains utilities to solve problems related to graphs and
trees
'''


def _get_max_height(tree):
    '''
    Function to determine the maximum height between the root and leaf
    of the tree

    Parameters
    ----------
    tree : pytools.graph_trees.BinaryTree obj
        tree to check for max height of

    Returns
    -------
    max_height : integer
        the maximum height of the provided tree
    '''

    # If passed in tree is None, return 0 for height
    if not tree or not (tree.left_child or tree.right_child):
        return 0

    # Get left and right leaf heights
    left_max = _get_max_height(tree.left_child)
    right_max = _get_max_height(tree.right_child)

    # Return 1 (since we made it past not check) + 
    # max of left/right children
    max_height = 1 + max([left_max, right_max])
    return max_height


def _get_min_height(tree):
    '''
    Function to determine the minimum height between the root and leaf
    of the tree

    Parameters
    ----------
    tree : pytools.graph_trees.BinaryTree obj
        tree to check for min height of

    Returns
    -------
    min_height : integer
        the minimum height of the provided tree
    '''

    # If passed in tree is None, return 0 for height
    if not tree or not (tree.left_child or tree.right_child):
        return 0

    # Get left and right leaf heights
    left_min = _get_min_height(tree.left_child)
    right_min = _get_min_height(tree.right_child)

    # Return 1 + (since we made it past not check)
    # max of left/right children
    min_height = 1 + min([left_min, right_min])
    return min_height


def check_tree_balanced(tree):
    '''
    This function checks to see if a binary tree is balanced, such that
    no two leaf nodes differ in distance from the root by more than one

    Parameters
    ----------
    tree : pytools.graph_trees.BinaryTree obj
        tree to check for min height of

    Returns
    -------
    balanced : boolean
        flag indiciating if input tree is balanced or not
    '''

    # Get max and min heights in tree
    max_height = _get_max_height(tree)
    min_height = _get_min_height(tree)

    # It is balanced if the difference is <= 1
    balanced = (max_height - min_height) <= 1

    # Return balance flag
    return balanced


def verify_tree_property(tree):
    '''
    Traverse through the tree and assert that the parent is greater
    than left child and less than right child
    '''

    # Init variables
    valid_l = True
    valid_r = True

    # Check left child recursively
    if tree.left_child:
        if tree.value < tree.left_child.value:
            return False
        valid_l = verify_tree_property(tree.left_child)

    # Check right child recursively
    if tree.right_child:
        if tree.value > tree.right_child.value:
            return False
        valid_r = verify_tree_property(tree.right_child)

    # Return True only if both right and left are True
    valid = (valid_l and valid_r)
    return valid


def binary_tree_from_arr(arr, start, end):
    '''
    Given a sorted array, build a binary tree of the values such that
    it has the minimum height: log_2(n)

    Parameters
    ----------
    arr : list
        a sorted list of numbers
    start : int
        the starting index to evaluate in list
    end : int
        the last index to evaluate in list

    Returns
    -------
    tree_node : pytools.graphs_trees.BinaryTree
        the populated tree node with left and right children populated
        correctly
    '''

    # Import packages
    from pytools.graphs_trees import trees

    # Check base case
    if end < start:
        return None

    # Get mid point and init tree node
    mid = (start+end)//2
    tree_node = trees.BinaryTree(arr[mid])

    # Recursively populate sub trees
    left_child = binary_tree_from_arr(arr, start, mid-1)
    right_child = binary_tree_from_arr(arr, mid+1, end)

    # Tie in left and right children
    tree_node.left_child = left_child
    tree_node.right_child = right_child

    # Return completed tree node
    return tree_node


def llists_from_bst(bst):
    '''
    Create a linked list for all of the nodes at each depth in the
    BinarySearchTree
    '''

    # Import packages
    from pytools.graphs_trees import trees
    from pytools.linked_lists import linked_lists

    # Error checking
    if not bst or not isinstance(bst, trees.BinarySearchTree):
        return []

    # Init variables
    llists = []
    llist = linked_lists.LinkedList()

    # Populate first linked list from root
    llist.insert(bst)
    llists.append(llist)

    # Iterate through llists
    for llist in llists:
        node = llist.head
        llist2 = linked_lists.LinkedList()
        while node:
            if node.data.left_child:
                llist2.insert(node.data.left_child)
            if node.data.right_child:
                llist2.insert(node.data.right_child)
            node = node.next_node
        if not llist2.head:
            break
        llists.append(llist2)

    # Convert linked lists of bst's to values
    for llist in llists:
        node = llist.head
        while node:
            node.data = node.data.value
            node = node.next_node

    return llists