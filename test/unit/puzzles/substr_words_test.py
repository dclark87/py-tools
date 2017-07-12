# test/unit/puzzles/substr_words_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on the substr_words
'''

# Import packages
import unittest

from pytools.puzzles import substr_words


class SubstrWordsTestCase(unittest.TestCase):
    '''
    TestCase for the substr_words.py module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        self.wdict = ['i', 'hat', 'hate', 'attention', 'tent', 'on', 'ion',
                      'eat', 'at', 'ten', 'a']
        self.instr = 'ihateattention'
        self.expected = [['i', 'hate', 'attention'],
                         ['i', 'hate', 'at', 'tent', 'i', 'on'],
                         ['i', 'hate', 'at', 'tent', 'ion'],
                         ['i', 'hat', 'eat', 'tent', 'i', 'on'],
                         ['i', 'hat', 'eat', 'tent', 'ion']]

    def test_substr_words(self):
        '''

        :return:
        '''

        outlist = substr_words.substr_words(self.instr, self.wdict)
        self.assertEqual(sorted(self.expected), sorted(outlist))

    def test_substr_words2(self):
        '''

        :return:
        '''

        outlist = substr_words.substr_words2(self.instr, self.wdict)
        self.assertEqual(sorted(self.expected), sorted(outlist))


# Main executable
if __name__ == '__main__':
    unittest.main()
