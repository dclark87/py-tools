# test/unit/stacks_queues/stacks_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on stacks module
'''

# Import packages
import unittest


class StacksTestCase(unittest.TestCase):
    '''
    TestCase for the stacks module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def _assert_stack(self, stack):
        '''
        Perform testing of stack's instance methods and assert
        proper functionality

        Parameters
        ----------
        stack : pytools.stacks_queues.Stack() obj
            the stack object can be a python list-implemented or a
            node-based, linked-list stack
        '''

        # Ensure it is empty
        err_msg = 'Stack should be empty!'
        self.assertTrue(stack.is_empty(), msg=err_msg)

        # Init items
        item1 = 42
        item2 = 420
        item3 = 4200

        # Push items on to stack
        stack.push(item1)
        stack.push(item2)
        stack.push(item3)

        # See stack has expected size
        err_msg = 'Length of stack should be 3, instead returned: %d'
        self.assertEqual(stack.size(), 3, msg=err_msg % stack.size())

        # Pop items off
        popped_item3 = stack.pop()
        popped_item2 = stack.pop()
        popped_item1 = stack.pop()

        # Assert items are being pushed/popped in correct order
        err_msg = 'Popped item: %d should equal %d'
        self.assertEquals(popped_item3, item3, msg=err_msg % (popped_item3, item3))
        self.assertEquals(popped_item2, item2, msg=err_msg % (popped_item2, item2))
        self.assertEquals(popped_item1, item1, msg=err_msg % (popped_item1, item1))

    def test_liststack(self):
        '''
        Test the python list-implementation of the stack
        '''

        # Import packages
        from pytools.stacks_queues import stacks

        # Init empty stack
        list_stack = stacks.ListStack()

        # Test instance methods
        self._assert_stack(list_stack)

    def test_nodestack(self):
        '''
        Test the node-based, linked-list implmentation of the stack
        '''

        # Import packages
        from pytools.stacks_queues import stacks

        # Init empty stack
        node_stack = stacks.NodeStack()

        # Test instance methods
        self._assert_stack(node_stack)


class MultiStackTestCase(unittest.TestCase):
    '''
    TestCase for the MultiStack object from the stacks module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_push_pop(self):
        '''
        Ensure we can push and pop from each stack within object
        '''

        # Import packages
        from pytools.stacks_queues import stacks

        # Init stack
        tri_stack = stacks.MultiStack(3)
        tri_stack.push('a', 0)
        tri_stack.push('b', 1)
        tri_stack.push('c', 1)
        tri_stack.push('d', 2)
        tri_stack.push('e', 0)
        tri_stack.push('f', 2)

        # Pop items
        c_char = tri_stack.pop(1)
        self.assertEqual(c_char, 'c')
        b_char = tri_stack.pop(1)
        self.assertEqual(b_char, 'b')
        self.assertRaises(IndexError, tri_stack.pop, 1)
        f_char = tri_stack.pop(2)
        self.assertEqual(f_char, 'f')
        e_char = tri_stack.pop(0)
        self.assertEqual(e_char, 'e')


if __name__ == '__main__':
    unittest.main()