# pytools/graphs_trees/utils.py
#
# Author: Daniel Clark, 2016

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
    if not tree:
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
    if not tree:
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