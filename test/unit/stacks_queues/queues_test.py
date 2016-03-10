# test/unit/stacks_queues/queues_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on stacks module
'''

# Import packages
import unittest


class QueuesTestCase(unittest.TestCase):
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

    def _assert_queue(self, queue):
        '''
        Perform testing of queue's instance methods and assert
        proper functionality

        Parameters
        ----------
        queue : pytools.stacks_queues.Queue() obj
            the queue object can be a python list-implemented or a
            node-based, linked-list stack
        '''

        # Ensure it is empty
        err_msg = 'Stack should be empty!'
        self.assertTrue(queue.is_empty(), msg=err_msg)

        # Init items
        item1 = 42
        item2 = 420
        item3 = 4200

        # Push items on to stack
        queue.enqueue(item1)
        queue.enqueue(item2)
        queue.enqueue(item3)

        # See stack has expected size
        err_msg = 'Length of queue should be 3, instead returned: %d'
        self.assertEqual(queue.size(), 3, msg=err_msg % queue.size())

        # Pop items off
        dequeued_item1 = queue.dequeue()
        dequeued_item2 = queue.dequeue()
        dequeued_item3 = queue.dequeue()

        # Assert items are being pushed/popped in correct order
        err_msg = 'Popped item: %d should equal %d'
        self.assertEquals(dequeued_item3, item3, msg=err_msg % (dequeued_item3, item3))
        self.assertEquals(dequeued_item2, item2, msg=err_msg % (dequeued_item2, item2))
        self.assertEquals(dequeued_item1, item1, msg=err_msg % (dequeued_item1, item1))

    def test_listqueue(self):
        '''
        Test the python list-implementation of the stack
        '''

        # Import packages
        from pytools.stacks_queues import queues

        # Init empty stack
        list_queue = queues.ListQueue()

        # Test instance methods
        self._assert_queue(list_queue)

    def test_nodequeue(self):
        '''
        Test the node-based, linked-list implmentation of the stack
        '''

        # Import packages
        from pytools.stacks_queues import queues

        # Init empty stack
        node_queue = queues.NodeQueue()

        # Test instance methods
        self._assert_queue(node_queue)


if __name__ == '__main__':
    unittest.main()