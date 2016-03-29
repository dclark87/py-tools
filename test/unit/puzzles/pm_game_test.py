# test/unit/puzzles/pm_game_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the puzzles/pm_game module
'''

# Import packages
import unittest


class PlusMinusGameTestCase(unittest.TestCase):
    '''
    TestCase for the Vertex class from the pm_game.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_list_moves(self):
        '''
        Method to test if player one can win or not given a start str
        '''

        # Import packages
        from pytools.puzzles import pm_game

        in_str = '----++--+-+++--'
        moves = ['++--++--+-+++--',
                 '-++-++--+-+++--',
                 '--++++--+-+++--',
                 '----+++++-+++--',
                 '----++--+-+++++']

        found_moves = pm_game.list_moves(in_str)
        self.assertEqual(found_moves, moves)

        in_str1 = '--++'
        p1_wins1 = pm_game.player_one_wins(in_str1)
        self.assertEqual(p1_wins1, False)
        in_str2 = '--++++--++---'
        p1_wins2 = pm_game.player_one_wins(in_str2)
        self.assertEqual(p1_wins2, False)


if __name__ == '__main__':
    unittest.main()