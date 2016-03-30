# pytools/linked_lists/utils.py
#
# Author: Daniel Clark, 2016

'''
This module contains utilities to solve problems related to linked
lists
'''

def remove_dups_llist(llist):
    '''
    Remove duplicate values from an unsorted linked list
    '''

    # Init variables
    count_dict = {}

    # Check for empty list
    node = llist.head
    if not node:
        print 'Input list is empty!'
        return llist

    # Start at second node
    next_node = node.next_node

    # While there are nodes in the list to analyze
    while next_node:
        if count_dict.has_key(next_node.data):
            node.next_node = next_node.next_node
        else:
            count_dict[next_node.data] = 1
            node = node.next_node
        next_node = node.next_node

    # Return list
    return llist


def is_llist_unique(llist):
    '''
    Return whether llist has all unique values or not
    '''

    # Init variables
    count_dict = {}

    # Check for empty list
    node = llist.head
    if not node:
        print 'Input list is empty!'
        return True

    # Start at second node
    next_node = node.next_node

    # While there are nodes in the list to analyze
    while next_node:
        if count_dict.has_key(next_node.data):
            return False
        else:
            count_dict[next_node.data] = 1
            node = node.next_node
        next_node = node.next_node

    # Return true if made it through loop
    return True