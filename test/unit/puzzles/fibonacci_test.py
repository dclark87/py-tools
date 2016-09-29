# test/unit/puzzles/fibonacci_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the fibonacci module
'''

# Import packages
import unittest


class FibonacciTestCase(unittest.TestCase):
    '''
    Test case for the fibonacci functions
    '''

    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_fibonacci(self):
        '''
        Test the non-recursive fibonacci function
        '''

        # Import packages
        from pytools.puzzles import fibonacci

        self.assertEqual(2, fibonacci.fibonacci(3))
        self.assertEqual(13, fibonacci.fibonacci(7))
        self.assertEqual(144, fibonacci.fibonacci(12))

    def test_fib(self):
        '''
        Test the recursive fibonacci function
        '''

        # Import packages
        from pytools.puzzles import fibonacci

        self.assertEqual(2, fibonacci.fib(3))
        self.assertEqual(13, fibonacci.fib(7))
        self.assertEqual(144, fibonacci.fib(12))


if __name__ == '__main__':
    unittest.main()
