# pytools/linked_lists/utils.py
#
# Author: Daniel Clark, 2016

'''
This module contains utilities to solve problems related to linked
lists
'''

def remove_dups_llist(llist):
    '''
    Remove duplicate values from an unsorted linked list using a dict
    external buffer for count
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


def remove_dups_llist_inplace(llist):
    '''
    Remove duplicate values from an unsorted linked list in-place
    '''

    # Init root, follower, leader
    root = llist.head
    follower = root
    leader = root.next_node

    # While root next is not null at end
    while root.next_node:
        # If leader is same as root, point follower to next
        if leader.data == root.data:
            follower.next_node = leader.next_node
        # Otherwise, move follower up
        # everything between follower and root is unique
        else:
            follower = leader

        # If leader points to null at end, move up root
        if not leader.next_node:
            root = root.next_node
            follower = root
            leader = root.next_node
        else:
            leader = leader.next_node

    # Return unique linked list
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


def find_n_tolast(llist, n):
    '''
    Find the nth-to-last element of a singly-linked list
    '''

    # Check error conditions
    if llist.size < n:
        raise ValueError('n must be smaller than size of list!')

    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a postive number')

    # Init variables
    ctr = 0
    thresh = llist.size - n
    node = llist.head

    # While ctr is less than thresh, continue searching
    while ctr < thresh:
        ctr += 1
        node = node.next_node

    # Return node data
    return node.data
