# pytools/puzzles/substr_words.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function to print every substring that is a word
in the passed in string, as long as the substring exists in the passed
in dictionary; the returned list of words must use all characters of
the original input string
'''


def substr_words(instr, wdict):
    '''
    Find all possible sub words sentences that use entire input word
    based on if those words exist in a dictionary, recursive approach

    :param instr:
    :param wdict:
    :return:
    '''

    outlist = []

    for i in xrange(1, len(instr)+1):
        substr = instr[:i]
        if substr not in wdict:
            continue
        if len(substr) < len(instr):
            outs = substr_words(instr[i:], wdict)
            for out in outs:
                if out:
                    outlist.append([substr] + out)
        else:
            outlist.append([substr])

    return outlist


def substr_words2(instr, wdict):
    '''
    Find all possible sub words sentences that use entire input word
    based on if those words exist in a dictionary, non-recursive,
    stack-based approach

    :param instr:
    :param wdict:
    :return:
    '''

    stack = [instr[0]]
    outlist = []
    i = 0
    while stack:
        word = stack.pop()
        while word not in wdict and i < len(instr)-1:
            i += 1
            word += instr[i]
        if i < len(instr)-1:
            stack.append(word)
            i += 1
            stack.append(instr[i])
        else:
            if word in wdict:
                out = stack + [word]
                outlist.append(out)
            i -= len(word)-1
            if len(stack) < 1:
                break
            stack.append(stack.pop()+instr[i])

    return outlist

