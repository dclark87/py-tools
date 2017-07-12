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


def _balanced(left, right, s, m):
    '''
    Recursive function to append to a list the balanced parentheses set
    computed by keeping track of an open and closed count

    :param left:
    :param right:
    :param s:
    :return:
    '''

    if left == 0 and right == 0:
        m.append(s)
    if left > 0:
        _balanced(left-1, right+1, s + '(', m)
    if right > 0:
        _balanced(left, right-1, s + ')', m)


def return_balanced(num):
    '''
    Function to return a list of balanced parentheses given number of
    pairs

    :param num:
    :return:
    '''

    out = []
    _balanced(num, 0, '', out)
    return out
