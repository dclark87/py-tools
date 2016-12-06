#
#
#

'''

'''

import unittest

from pytools.puzzles import student_prizes

class StudentPrizesTestCase(unittest.TestCase):
    '''

    '''

    def test_student_prizes(self):
        '''

        :return:
        '''

        # Import packages
        import itertools

        # Init variables
        n = 3
        letters = 'ALO'
        expected = len(list(itertools.product(letters, repeat=n)))

        returned = student_prizes.prize_combos(n)

        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()