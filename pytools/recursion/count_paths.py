# pytools/recursion/count_paths.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function to count the possible paths through a
grid
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
