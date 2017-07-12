# pytools/puzzles/two_trees_leaves.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function that finds the difference between two trees
leaves nodes - first pair of non-matching leaves
'''


def first_pair_nonmatch(tree1, tree2):
    '''
    Find the first pair of non-matching leaves between two trees

    :param tree1:
    :param tree2:
    :return:
    '''

    stack = [tree1]
    leaves1 = []

    while len(stack) > 0:
        node = stack.pop()
        if node.right_child:
            stack.append(node.right_child)
        if node.left_child:
            stack.append(node.left_child)
        if not (node.left_child or node.right_child):
            leaves1.append(node)

    stack = [tree2]
    leaves2 = []
    while len(stack) > 0:
        node = stack.pop()
        if node.right_child:
            stack.append(node.right_child)
        if node.left_child:
            stack.append(node.left_child)
        if not (node.left_child or node.right_child):
            leaves2.append(node)

    for i, leaf in enumerate(leaves1):
        leaf2 = leaves2[i]
        if leaf.value != leaf2.value:
            return (leaf.value, leaf2.value)