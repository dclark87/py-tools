# pytools/recursion/parentheses.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to return the number of valid
parentheses pairs given a number of pairs
'''


def _pairs(left, right=None):
    '''
    '''

    if right is None:
        right = left
    if left == right == 0:
        yield ''
    else:
        if left > 0:
            for p in _pairs(left-1, right):
                yield '(' + p
        if right > left:
            for p in _pairs(left, right-1):
                yield ')' + p


def parenth_pairs(pairs):
    '''
    Function to return the number of valid parentheses pairs given a
    number of pairs

    Parameters
    ----------
    pairs : int
        integer of number of pairs combinations to produce
    '''

    return list(_pairs(pairs, pairs))