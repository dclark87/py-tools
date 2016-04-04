# pytools/puzzles/abbadiv1.py
#
# Author: Daniel Clark, 2016

'''
This module contains the ABBADiv1 class problem and solution from
Topcoder.com
'''


class ABBADiv1(object):
    '''
    Mandatory class definition for problem
    '''

    def can_obtain(self, initial, target):
        '''
        Convert initial to target via:
        1) Can add "A" to end of initial
        2) Can add "B" followed by reversing inital
        '''

        if len(target) < len(initial):
            return 'Impossible'
        if initial == target:
            return 'Possible'
        if target.startswith('A') and initial.startswith('B'):
            return 'Impossible'
        initial_xfm = initial
        while initial_xfm != target:
            if initial_xfm + 'A' in target or initial_xfm + 'A' in target[::-1]:
                initial_xfm = initial_xfm + 'A'
            elif (initial_xfm + 'B')[::-1] in target or (initial_xfm + 'B')[::-1] in target[::-1]:
                initial_xfm = (initial_xfm + 'B')[::-1]
            else:
                return 'Impossible'
        return "Possible"