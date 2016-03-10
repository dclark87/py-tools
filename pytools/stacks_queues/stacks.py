# pytools/stacks_queues/stacks.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to stacks
'''

class ListStack(object):
    '''
    Last in, first out queue of objects using built-in Python list
    '''

    def __init__(self, item=None):
        '''
        Init the list-style stack
        '''
        if item:
            self.items = [item]
        else:
            self.items = []

    def pop(self):
        '''
        Pop off the top (last in) item from the stack
        '''
        return self.items.pop()

    def push(self, item):
        '''
        Push item on to top of stack
        '''
        self.items.append(item)

    def size(self):
        '''
        Get size of stack
        '''
        return len(self.items)

    def is_empty(self):
        '''
        Check to see if stack is empty
        '''
        if len(self.items) == 0:
            return True
        else:
            return False


class Node(object):
    '''
    '''

    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node=None):
        self.set_next = next_node

    def get_item(self):
        return self.item

    def set_item(self, item=None):
        self.item = item


class NodeStack(object):
    '''
    Last in, first out (LIFO) queue of objects using Node class
    '''

    def __init__(self, item=None):
        '''
        Init the Node-style stack
        '''

        if item:
            node = Node(item=item, next_node=None)
            self.head = node
        else:
            self.head = None

    def pop(self):
        '''
        Pop off the top (last in) item from the stack
        '''

        # Return head node if it exists
        if self.head:
            head_node = self.head
            # Set head now to popped node's next node
            self.head = head_node.get_next()
        # If head doesn't exist, return index error
        else:
            err_msg = 'Trying to pop from empty list!'
            raise IndexError(err_msg)

        # Return head node's item value
        return head_node.item

    def push(self, item):
        '''
        Push item on to top of stack
        '''

        # Create new node to store item and point to current head
        new_head = Node(item=item, next_node=self.head)
        # Set head to new node
        self.head = new_head

    def size(self):
        '''
        Get size of stack
        '''

        # Init variables
        count = 0
        curr_node = self.head

        # While the nodes still exist
        while curr_node:
            count += 1
            curr_node = curr_node.get_next()

        # Return count
        return count

    def is_empty(self):
        '''
        Check to see if stack is empty
        '''

        if not self.head:
            return True
        else:
            return False
