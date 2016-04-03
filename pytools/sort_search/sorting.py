# pytools/sort_search/sorting.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''


def _check_numeric(input_arr):
    '''
    Check all elements of the array are numeric
    '''

    # Check input is numeric
    for val in input_arr:
        if not (isinstance(val, int) or isinstance(val, float)):
            err_msg = 'All values in input array must be numeric! Found: %s' \
                      % str(val)
            raise ValueError(err_msg)

def merge_sort(input_arr):
    '''
    Function to sort an input array of numeric data via the merge
    sort algorithm
    '''

    # Check for numeric types
    _check_numeric(input_arr)

    len_arr = len(input_arr)
    sorted_arr = []
    if len_arr > 2:
        mid = len_arr//2
        left_sorted = merge_sort(input_arr[:mid])
        right_sorted = merge_sort(input_arr[mid:])
        # Compare two array elements and sort
        left_idx = right_idx = 0
        while len(sorted_arr) < (len(left_sorted) + len(right_sorted)):
            left_el = left_sorted[left_idx]
            right_el = right_sorted[right_idx]
            if left_el <= right_el:
                sorted_arr.append(left_el)
                left_idx += 1
                if left_idx == len(left_sorted):
                    sorted_arr.extend(right_sorted[right_idx:])
            else:
                sorted_arr.append(right_el)
                right_idx += 1
                if right_idx == len(right_sorted):
                    sorted_arr.extend(left_sorted[left_idx:])
    # 2 or less elements
    else:
        # 1 element, just append
        if len_arr == 1:
            sorted_arr.append(input_arr[0])
        else:
            if input_arr[0] > input_arr[1]:
                smaller = input_arr[1]
                larger = input_arr[0]
            else:
                smaller = input_arr[0]
                larger = input_arr[1]
            sorted_arr.append(smaller)
            sorted_arr.append(larger)

    # Return the sorted array
    return sorted_arr


def quick_sort(input_arr):
    '''
    Function to sort an input array of numeric data via the quick
    sort algorithm
    '''

    # Check for numeric types
    _check_numeric(input_arr)

    # Base case of length 0 or 1
    if len(input_arr) == 0 or len(input_arr) == 1:
        return input_arr

    # Init pivot and left and right marks
    pivot = 0
    leftmark = 1
    rightmark = len(input_arr)-1
    done = False

    while not done:
        # Increment left mark as long as its less than pivotval
        while input_arr[leftmark] < input_arr[pivot] and leftmark <= rightmark:
            leftmark += 1

        # Decrement right mark as long as its less than pivotval
        while input_arr[rightmark] >= input_arr[pivot] and rightmark >= leftmark:
            rightmark -= 1

        if rightmark >= leftmark:
            tmp = input_arr[leftmark]
            input_arr[leftmark] = input_arr[rightmark]
            input_arr[rightmark] = tmp
        else:
            done = True

    # Marks passed eachother, new pivot point
    tmp = input_arr[pivot]
    input_arr[pivot] = input_arr[rightmark]
    input_arr[rightmark] = tmp
    pivot = rightmark

    # Recursively call on left and right of pivot
    left_sorted = quick_sort(input_arr[:pivot+1])
    right_sorted = quick_sort(input_arr[pivot+1:])

    # Merge two sorted subarrays together
    output_arr = left_sorted
    output_arr.extend(right_sorted)

    # Return merged and sorted array
    return output_arr