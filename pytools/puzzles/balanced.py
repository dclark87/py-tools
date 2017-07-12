# pytools/puzzles/balanced.py
#
# Author: Daniel Clark, 2016

'''

'''

def is_balanced(s):
    '''

    :param s:
    :return:
    '''

    braces = ('{', '}')
    brackets = ('[', ']')
    parenths = ('(', ')')
    stack = []

    # For each char in string
    for c in s:
        if c in braces:
            pair = braces
        elif c in brackets:
            pair = brackets
        elif c in parenths:
            pair = parenths
        else:
            continue

        # Found closing bracket, check stack
        if c == pair[1]:
            if len(stack) < 1 or c != stack.pop():
                return False
            else:
                continue
        # Open bracket
        else:
            stack.append(pair[1])

    # Check stack
    if len(stack) > 0:
        return False
    else:
        return True