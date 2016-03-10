# linked_lists/linked_lists.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to linked
lists
'''

class Node(object):
    '''
    '''

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node


class LinkedList(object):
    '''
    '''

    def __init__(self, head=None):
        '''
        Init list head
        '''

        # Point head of list
        self.head = head

    def insert(self, data):
        '''
        Insert node with data into list
        '''

        # Init Node obj and point head of list to it
        node = Node(data, self.head)
        self.head = node

    def size(self):
        '''
        Return the number of nodes in list
        '''

        # Init variables
        current_node = self.head
        count = 0

        # Iterate through list until we get None
        while current_node:
            count += 1
            current_node = current_node.get_next()

        # Return total count
        return count

    def find_node(self, data):
        '''
        Find node with specified data attribute
        '''

        # Init variables
        current_node = self.head
        found = False

        # Parse through list
        while current_node and not found:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()

        # Node containing data is not in list
        if current_node is None:
            raise ValueError('node not found containing data: %s' % str(data))
        else:
            return current_node

    def delete_node(self, data):
        '''
        Delete node with specified data attribute
        '''

        # Init variables
        current_node = self.head
        prev_node = None
        found = False

        # Parse through list
        while current_node and not found:
            if current_node.get_data() == data:
                found = True
            else:
                prev_node = current_node
                current_node = current_node.get_next()

        # Node containing data is not in list
        if not current_node:
            raise ValueError('node not found containing data: %s' % str(data))
        # If prev_node stays None, data was in head - set to current's next
        if not prev_node:
            self.head = current_node.get_next()
        # Otherwise, set prev_node's next to current's next
        else:
            prev_node.set_next(current_node.get_next())