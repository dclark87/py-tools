# pytools/puzzles/reverse_integer.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function to reverse an integer
'''

# Import packages
import math


def _rev(d, m):
    '''

    :param d:
    :param m:
    :return:
    '''

    # Get nearest 10th exponent
    b = int(math.log10(d))
    e = 10**b
    dd = d//e
    m.insert(0, dd)
    nextd = d-dd*e

    # Account for any intermediary zeros
    while (nextd != 0) and (int(math.log10(nextd)) != b-1):
        m.insert(0, 0)
        b -= 1
    if b == 0:
        return m
    else:
        return _rev(d-dd*e, m)


def reverse_integer(d):
    '''
    Function to reverse an integer

    :param d:
    :return:
    '''

    revlist = _rev(d, [])
    out = 0
    e = len(revlist)-1
    for num in revlist:
        out += (10**e)*num
        e -= 1

    return out
