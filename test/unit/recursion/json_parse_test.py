# test/unit/recursion/json_parse_test.py
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on recursion/json_parse module
'''

# Import packages
import unittest

from pytools.recursion import json_parse

class JsonParseTestCase(unittest.TestCase):
    '''
    TestCase for the json_parse function
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''
        pass

    def test_json_parse(self):
        json = {'k1': [{'k2': [['hi', 'there'], ['old']]}]}
        expected_json = {'k1': [{'k2': [['hi', 'there'], ['new']]}]}
        key_str = 'k1.k2'
        json_parse.json_parse(json, key_str, 'old', 'new')
        self.assertEqual(expected_json, json)

if __name__ == '__main__':
    unittest.main()
