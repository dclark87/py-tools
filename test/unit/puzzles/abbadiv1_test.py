# test/unit/puzzles/abbadiv1_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on puzzles/abbadiv1 module
'''

# Import packages
import unittest


class ABBADiv1TestCase(unittest.TestCase):
    '''
    TestCase for the abbadiv1 module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def test_can_obtain(self):
        '''
        Test the initial -> target can_obtain method
        '''

        # Import packages
        from pytools.puzzles import abbadiv1

        # Init variables
        abba_div1 = abbadiv1.ABBADiv1()
        initial = 'AAABBAABB'
        target = 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'

        can_obtain = abba_div1.can_obtain(initial, target)
        self.assertEquals(can_obtain, 'Possible')


if __name__ == '__main__':
    unittest.main()