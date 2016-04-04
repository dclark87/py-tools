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


class StackNode(object):
    '''
    StackNode object to use for the TriStack class; contains data and
    an integer corresponding to the position of the next Node in the
    TriStack array
    '''

    def __init__(self, data, next_idx=None):
        '''
        Init the StackNode object
        '''

        self.data = data
        self.next_idx = next_idx


class MultiStack(object):
    '''
    Stack object that keeps multiple stacks in a single array
    '''

    def __init__(self, num_stacks=3):
        '''
        Init empty TriStack object
        '''
        self.heads = [None]*num_stacks
        self.array = []

    def push(self, data, stack_num):
        '''
        Add a new node to the stack specified by stack_num
        '''

        # Check for usage errors
        if stack_num < 0 or stack_num >= len(self.heads):
            raise ValueError('invalid stack num!')

        # Get current head index
        head = self.heads[stack_num]
        node = StackNode(data=data, next_idx=head)
        self.array.append(node)
        self.heads[stack_num] = len(self.array)-1

    def pop(self, stack_num):
        '''
        Pop latest data from stack specified by stack_num; this
        algorithm approaches the problem with memory conservation in
        mind as it keeps the size of the array to as small as possible
        instead of letting it grow and setting popped-values to None
        '''

        # Check for usage errors
        if stack_num < 0 or stack_num >= len(self.heads):
            raise ValueError('invalid stack num!')

        # Get head index
        head = self.heads[stack_num]
        # If head is not None, pop off item
        if head:
            node = self.array.pop(head)
            # Decrement each node whos next_idx > head
            for snode in self.array:
                if snode.next_idx > head:
                    snode.next_idx -= 1
            for idx, val in enumerate(self.heads):
                if val > head:
                    self.heads[idx] = val-1
            self.heads[stack_num] = node.next_idx

        else:
            raise IndexError('no items left on stack: %d!' % stack_num)

        # Return node data
        return node.data