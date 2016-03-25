# pytools/sort_search/sorting.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''

def merge_sort(input_arr):
    '''
    Function to sort an input array of numeric data via the merge
    sort algorithm
    '''

    # Check for numeric types
    for el in input_arr:
        if not (isinstance(el, int) or isinstance(el, float)):
            err_msg = 'Element: %s is not numeric!' % str(el)
            raise ValueError(err_msg)

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


def quick_sort(input_arr, first=None, last=None):
    '''
    Function to sort an input array of numeric data via the quick
    sort algorithm
    '''

    # Check for numeric types
    for el in input_arr:
        if not (isinstance(el, int) or isinstance(el, float)):
            err_msg = 'Element: %s is not numeric!' % str(el)
            raise ValueError(err_msg)

    if not first:
        first = 0
    if not last:
        last = len(input_arr)-1
    if first < last:
        split_point = _partition(input_arr, first, last)
        quick_sort(input_arr, first, split_point-1)
        quick_sort(input_arr, split_point+1, last)

    return input_arr

def _partition(input_arr, first, last):
    '''
    '''

    pivot = input_arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and input_arr[leftmark] <= pivot:
            leftmark += 1
        while input_arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = input_arr[leftmark]
            input_arr[leftmark] = input_arr[rightmark]
            input_arr[rightmark] = temp
    temp = input_arr[first]
    input_arr[first] = input_arr[rightmark]
    input_arr[rightmark] = temp

    return rightmark