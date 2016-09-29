# pytools/puzzles/fibonacci.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions for performing the fibonacci sequence
'''


def fibonacci(num):
    '''
    Return the Fibonacci number for the integer provided, non-revursive

    Parameters
    ----------
    num : int
        the number of the Fibonacci sequence to calculate

    Returns
    -------
    fsum : int
        the num-th integer in the Fibonacci sequence
    '''

    # Error case
    if not isinstance(num, int) or num < 1:
        raise Exception('Invalid input!')

    # Base case
    if num < 3:
        return 1

    # Iterate through and accumulate
    prev1 = 1
    prev2 = 1
    fsum = 0
    for i in xrange(3, num+1):
        fsum = prev1 + prev2
        prev2 = prev1
        prev1 = fsum

    # Return the sum
    return fsum


def fib(num):
    '''
    Return the Fibonacci number for the integer provided, revursive

    Parameters
    ----------
    num : int
        the number of the Fibonacci sequence to calculate

    Returns
    -------
    fsum : int
        the num-th integer in the Fibonacci sequence
    '''

    # Error case
    if not isinstance(num, int) or num < 1:
        raise Exception('Invalid input!')

    # Base case
    if num < 3:
        return 1
    else:
        return fib(num-2) + fib(num-1)