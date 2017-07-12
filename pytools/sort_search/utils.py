# pytools/sort_search/a_merge_b.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function which merges two sorted lists together
in place
'''

def a_merge_b(a_arr, b_arr):
    '''
    Assume A and B are sorted arrays where A has an empty buffer at the
    end big enough to store B; merge the two together as one sorted
    array (in place)

    Parameters
    ----------
    a_arr : list
        sorted list of integers
    b_arr : list
        sorted list of integers

    Returns
    -------
    a_arr : list
        the merged and sorted list of integers from A and B
    '''

    # Check data types
    if not isinstance(a_arr, list) or not isinstance(b_arr, list):
        raise ValueError('A and B must be lists!')

    # Find first index of None
    for n_idx, aval in enumerate(a_arr):
        if aval is None:
            break

    if len(b_arr) > len(a_arr) - n_idx:
        raise ValueError('B must be able to fit in None buffer of A')

    # Init variables
    m_idx = len(a_arr)-1
    a_idx = n_idx-1
    b_idx = len(b_arr)-1

    # Populate a_arr from end to beg
    while a_idx >= 0 and b_idx >= 0:
        # If bval is greater, b -> a, decrement bidx
        if b_arr[b_idx] > a_arr[a_idx]:
            a_arr[m_idx] = b_arr[b_idx]
            b_idx -= 1
        # Else, aval is greater, a -> a, decrement aidx
        else:
            a_arr[m_idx] = a_arr[a_idx]
            a_idx -= 1
        # Decrement merged index
        m_idx -= 1

    # If there are any bvals left, they must be smallest
    # Throw in beginning of a_arr
    while b_idx >= 0:
        a_arr[b_idx] = b_arr[b_idx]
        b_idx -= 1

    # Return a_arr
    return a_arr


def rot_arr_search(rot_arr, elem):
    '''
    Function to find an element in an originally sorted, but rotated
    array in O(logn)

    Parameters
    ----------
    rot_arr : list
        a list of numbers that are sorted but rotated
    elem : int or float
        element of list to find

    Returns
    -------
    pos : int
        position of element in rot_arr
    '''

    # Init variables
    low = 0
    high = len(rot_arr)-1

    # While the extrema indices are in order
    while low <= high:
        mid = (high+low)//2
        # If we found right element
        if rot_arr[mid] == elem:
            # Return its index
            return mid
        # Othwerwise if the low elem <= high elem (in sorted section)
        elif rot_arr[low] <= rot_arr[high]:
            # If element > mid, move low up to mid+1
            if elem > rot_arr[mid]:
                low = mid + 1
            # If elem >= low elem, move high to mid-1
            elif elem >= rot_arr[low]:
                high = mid - 1
            else:
                low = mid + 1
        # If element is less than mid, move high to mid-1
        elif elem < rot_arr[mid]:
            high = mid - 1
        # If element is <= high, move low to mid+1
        elif elem <= rot_arr[high]:
            low = mid + 1
        else:
            high = mid - 1

    # While loop terminated without finding elem, raise error
    raise KeyError('elem: %s not found!' % str(elem))
