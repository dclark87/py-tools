# pytools/arrays_strings/arrays.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to array
manipulation and testing
'''

def flips(q, n, mat):
    '''
    :param q: number of flips
    :param n: where matrix is 2n x 2n
    :param mat: the matrix (can be plain array)
    :return:
    '''

    # Import packages
    import numpy as np

    # Init variables
    mat = np.matrix(mat)
    q_moves = []
    while q > 0:
        # Create a list of tuples, [(
        for i in xrange(n):
            upper_sum = mat[:n/2, i]
            lower_sum = mat[n/2:, i]
            left_sum = mat[i, :n/2]
            right_sum = mat[i, n/2:]
            sums = [upper_sum, lower_sum, left_sum, right_sum]
            max_idx = np.argmax(sums)
            if max_idx == 0:
                q_moves.append(('col', False, upper_sum))
            elif max_idx == 1:
                q_moves.append(('col', True, lower_sum))
            elif max_idx == 2:
                q_moves.append(('row', False, left_sum))
            elif max_idx == 3:
                q_moves.append(('row', True, right_sum))


