# pytools/recursion/subsets.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to return all of the subsets of a given
set
'''


def subsets_reduce(input_set):
    '''
    Reduce function method for returning all subsets of a set
    '''

    return reduce(lambda z, x: z + [y + [x] for y in z],
                  input_set, [[]])


def subsets(input_set):
    '''
    Return all subsets of a given set by returning a generator
    '''

    # Init list set
    list_set = list(input_set)

    # If it's < 1, yield itself and break
    if len(list_set) < 1:
        yield list_set
        return

    # Return last element from list as a list of 1
    el = [list_set.pop()]
    # We can iterate over a generator
    for sub in subsets(list_set):
        yield sub
        yield sub+el


def subsets_binary(input_set):
    '''
    Iterate through all combinations of yes/no for each item in set
    via a bit mask combination
    '''

    # Init maximum subset size
    max_num = 1 << len(input_set)
    all_subsets = []

    # For each subset
    for num in range(max_num):
        # Init subset
        subset = []
        mask = num
        idx = 0

        # While mask has some 1's in it
        while mask > 0:
            # If LSB is set, grab set at idx
            if (mask & 1) > 0:
                subset.append(input_set[idx])
            # Shift mask down one
            mask >>= 1
            # Reflect mask shift by incrementing index we'll grab next time
            idx += 1

        # And add newly compounded subset to output
        all_subsets.append(subset)

    # Return all subsets found
    return all_subsets