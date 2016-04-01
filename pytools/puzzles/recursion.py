# pytools/puzzles/recursion.py
#
# Author: Daniel Clark, 2016

'''
This module contains utilities to solve puzzles related to recursion
'''


def count_paths(n, x, y):
    '''
    Function to count the total number of paths in an nxn grid one can
    take by traversing only downwards and right to get from point (x,y)
    to the lower right hand corner (n,n) of the grid

    Parameters
    ----------
    n : integer
        dimension of the grid = nxn
    x : integer
        x-coordinate to count paths from
    y : integer
        y-coordinate to count paths from

    Returns
    -------
    xy_paths : integer
        the total possible number of paths from (x,y) to (n,n)
    '''

    # If we're passed n < 1, raise error
    if n < 1:
        raise ValueError('grid size must be > 0!')

    # Init paths
    x_paths = 0
    y_paths = 0

    # x paths
    if n-x > 1:
        x_paths += count_paths(n, x+1, y)
    elif n-x == 1:
        x_paths = 1

    # y paths
    if n-y > 1:
        y_paths += count_paths(n, x, y+1)
    elif n-y == 1:
        y_paths = 1

    # Return total paths for x and y
    tot_paths = x_paths + y_paths
    return tot_paths


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