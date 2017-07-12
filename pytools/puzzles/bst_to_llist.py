# pytools/puzzles/bst_to_llist.py
#
# Author: Daniel Clark, 2016

'''
Module containing a function to turn a binary search tree into a sorted,
circular linked list
'''


class DLNode(object):
    def __init__(self, value):
        self.value = value
        self._prev = None
        self._next = None


def bst_to_llist(root):
    '''
    Function to build a doubly-linked list, sorted, and circular from a
    binary search tree, via an in-order traversal (non-recursive) in O(n) time

    :param root:
    :return:
    '''

    # Traverse tree in-order
    stack = []
    node = root
    done = False
    head = None

    while not done:
        if node:
            stack.append(node)
            node = node.left_child
        else:
            if len(stack) > 0:
                node = stack.pop()
                if not head:
                    head = DLNode(node.value)
                    prev = head
                else:
                    new = DLNode(node.value)
                    new._prev = prev
                    prev._next = new
                    prev = new
                node = node.right_child
            else:
                head._prev = new
                new._next = head
                done = True

    return head