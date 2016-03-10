# pytools/stacks_queues/queues.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to stacks
'''

class ListQueue(object):
    '''
    Queue implemented with Python built-in list
    '''

    def __init__(self, item=None):
        '''
        init Queue instance
        '''

        self.items = []

        if item:
            self.items.append(item)

    def enqueue(self, item):
        '''
        insert item into queue
        '''

        self.items.insert(0, item)

    def dequeue(self):
        '''
        return oldest item from queue
        '''

        return self.items.pop()

    def size(self):
        '''
        Get size of queue
        '''

        return len(self.items)

    def is_empty(self):
        '''
        check if queue is empty
        '''

        return len(self.items) == 0


class Node(object):
    '''
    Linked-list type Node object
    '''

    def __init__(self, item=None, next_node=None, prev_node=None):
        '''
        init the Node instance
        '''

        self._item = item
        self._prev_node = prev_node

    def set_prev(self, prev_node):
        '''
        set previous node
        '''
        self._prev_node = prev_node

    def get_prev(self):
        '''
        get previous node
        '''
        return self._prev_node

    def get_item(self):
        '''
        get the node item
        '''
        return self._item


class NodeQueue(object):
    '''
    Queue implemented with linked-list style Nodes
    '''

    def __init__(self, item=None):
        '''
        init Queue instance
        '''

        if item:
            head_node = Node(item=item, next_node=None)
            self.head = head_node
            self.tail = None
        else:
            self.head = None
            self.tail = None

    def enqueue(self, item):
        '''
        insert item into queue
        '''

        node = Node(item=item, prev_node=None)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.set_prev(node)
        self.tail = node

    def dequeue(self):
        '''
        return oldest item from queue
        '''

        head_node = self.head
        self.head = head_node.get_prev()

        return head_node.get_item()

    def size(self):
        '''
        Get size of queue
        '''

        counter = 0
        curr_node = self.head
        while curr_node:
            counter += 1
            curr_node = curr_node.get_prev()
            
        return counter

    def is_empty(self):
        '''
        check if queue is empty
        '''

        if not self.head:
            return True
        else:
            return False
