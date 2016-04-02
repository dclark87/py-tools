# test/unit/recursion/count_paths_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/subsets module
'''

# Import packages
import unittest


class SubsetsTestCase(unittest.TestCase):
    '''
    TestCase for the subsets method
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def test_subsets(self):
        '''
        Test the count_paths function
        '''

        # Import packages
        from pytools.recursion import subsets

        # Init variables
        set1 = 'abc'

        # Get generator and create list of subsets
        ssgen1 = subsets.subsets(set1)
        subsets1 = sorted([sub for sub in ssgen1])
        # Create list of subsets via reduce function
        subsets2 = sorted(subsets.subsets_reduce(set1))

        # Assert they agree
        self.assertEqual(subsets1, subsets2)

        # Get subsets via binary method
        subsets3 = sorted(subsets.subsets_binary(set1))
        # Assert they agree
        self.assertEqual(subsets1, subsets3)


if __name__ == '__main__':
    unittest.main()