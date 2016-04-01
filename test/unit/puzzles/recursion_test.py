# test/unit/puzzles/recursion_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on puzzles/recursion module
'''

# Import packages
import unittest


class CountPathsTestCase(unittest.TestCase):
    '''
    TestCase for the utils module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def _combinations(self, n):
        '''
        Calculate how many possible paths there are in the down-right
        game for an n x n grid, starting as position (1,1). Each path
        has n-1 + n-1 moves. We can uniquely identify each possible
        path by knowing at which steps we move right. We always move
        right n-1 times out of 2n-2 steps;
        combinations of n-1 times out of 2n-2:
        n_C_r = n!/r!(n-r)! -> 2n-2_C_n-1 = 2n-2! / ((n-1)!*(n-1)!)
        '''

        # Import packages
        import math

        # Return combinations
        total_paths = math.factorial(2*n-2) / \
                      (math.factorial(n-1) * math.factorial(n-1))
        return total_paths


    def test_count_paths(self):
        '''
        Test the count_paths function
        '''

        # Import packages
        from pytools.puzzles import recursion


        # Get total paths
        total_paths = self._combinations(5)
        paths = recursion.count_paths(5, 1, 1)
        self.assertEqual(paths, total_paths)


if __name__ == '__main__':
    unittest.main()