# pytools/recursion/power.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to find the power given a base and
exponent using recursion
'''

def power(base, exp):
    '''

    :param base:
    :param exp:
    :return:
    '''

    if exp == 0:
        return 1
    else:
        d = power(base, abs(exp)-1)
        if abs(exp) != exp:
            return 1/(d*base)
        else:
            return d*base