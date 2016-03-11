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
        # Check node inputs
        if prev_node and not isinstance(prev_node, Node):
            err_msg = 'prev_node should be Node type, not type %s' \
                      % str(type(prev_node))
            raise ValueError(err_msg)
        if next_node and not isinstance(next_node, Node):
            err_msg = 'next_node should be Node type, not type %s' \
                      % str(type(next_node))
            raise ValueError(err_msg)

        self._item = item
        self._prev_node = prev_node
        self._next_node = next_node

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

    def set_next(self, next_node):
        '''
        set next node
        '''
        self._next_node = next_node

    def get_next(self):
        '''
        get next node
        '''
        return self._next_node

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


class ListDequeue(object):
    '''
    Double-ended queue using Python built-in lists
    '''

    def __init__(self, item=None):
        '''
        init double-ended queue
        '''
        if item:
            self.items = [item]
        else:
            self.items = []

    def add_to_head(self, item):
        '''
        push item onto dequeue
        '''
        self.items.append(item)

    def pop_from_head(self):
        '''
        pop item from head of queue
        '''
        return self.items.pop()

    def add_to_tail(self, item):
        '''
        insert item into dequeue
        '''
        self.items.insert(0, item)

    def pop_from_tail(self):
        '''
        pop item from tail of queue
        '''
        return self.items.pop(0)


class NodeDequeue(object):
    '''
    Double-ended queue using Node class
    '''

    def __init__(self, item=None):
        '''
        init double-ended queue
        '''
        if item:
            node = Node(item=item, next_node=None, prev_node=None)
            self.head = node
            self.tail = node
        else:
            self.head = None
            self.tail = None

    def add_to_head(self, item):
        '''
        push item onto dequeue
        '''
        node = Node(item=item, next_node=None, prev_node=self.head)
        self.head = node

        if not self.tail:
            self.tail = node

    def pop_from_head(self):
        '''
        pop item from head of queue
        '''
        head_node = self.head
        self.head = head_node.get_prev()
        return head_node.get_item()

    def add_to_tail(self, item):
        '''
        insert item into dequeue
        '''
        node = Node(item=item, next_node=self.tail, prev_node=None)
        self.tail = node

        if not self.head:
            self.head = node

    def pop_from_tail(self):
        '''
        pop item from tail of queue
        '''
        tail_node = self.tail
        self.tail = tail_node.get_next()
        return tail_node.get_item()








