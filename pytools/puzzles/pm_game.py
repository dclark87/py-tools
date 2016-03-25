# pytools/puzzles/pm_game.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve various puzzles and games
'''


def list_moves(input_str):
    '''
    Given an input string for plus-minus game, list all possible moves
    '''

    # Init variables
    moves = []

    # Iterate through input string to search for '--'
    for idx, char in enumerate(input_str):
        if idx < len(input_str)-1:
            if char == '-' and input_str[idx+1] == '-':
                move = list(input_str)
                move[idx] = '+'
                move[idx+1] = '+'
                move = ''.join(move)
                moves.append(move)

    # Return moves
    return moves


def player_one_wins(input_str):
    '''
    In the plus-minus game, return if there is a change for player
    1 to win or not
    '''

    # Get a list of moves
    moves = list_moves(input_str)
    print 'player moves: %s' % str(moves)

    # If there are no available moves, assume player 1 wins
    if len(moves) == 0:
        return True
    # If there is one available move, player 1 loses
    elif len(moves) == 1:
        return False

    p1_move_wins = []
    # Explore each move
    for move in moves:
        print '---move--- %s' % str(move)
        p1_wins = player_one_wins(move)
        p1_move_wins.append(p1_wins)
    if True in p1_move_wins:
        return True
    else:
        return False
    # Return not p1_wins
    # Even number of recursive calls will result in keeping flag
    # the same, odd will be different
    # Even calls with no moves left at end 
    #return not p1_wins