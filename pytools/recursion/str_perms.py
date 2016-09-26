# pytools/recursion/str_perms.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function to find all permutations of a string
'''

def permutations(in_str):
    '''
    Create a list of all the permutations of a string
    '''

    # Error checking
    if not isinstance(in_str, str):
        raise ValueError('input must be string!')

    # Base cases
    if len(in_str) == 0:
        return ''
    if len(in_str) == 1:
        return in_str

    # Grab first character and rest of characters
    first_char = in_str[0]
    rest_chars = in_str[1:]

    # Get perms of sub string rest of chars
    sub_perms = permutations(rest_chars)

    # Iterate through each perm and insert first char at all locs
    perms = []
    for subp in sub_perms:
        idx = 0
        while idx <= len(subp):
            perm = subp[:idx] + first_char + subp[idx:]
            perms.append(perm)
            idx += 1

    # Return perms
    return perms
