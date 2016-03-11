# test/unit/sort_search/hash_tables_test
#
# Author: Daniel Clark, 2016

'''
Unit test module to perform testing on hash_tables module
'''

# Import packages
import unittest


class HashTableTestCase(unittest.TestCase):
    '''
    TestCase for the hash_tables module
    '''

    # Set up test case
    def setUp(self):
        '''
        Initialize test case with attributes
        '''

        # Init instance attributes
        pass

    def test_hash_put_get(self):
        '''
        Test hash table can put and get key/value pairs
        '''

        # Import packages
        from pytools.sort_search import hash_tables

        # Init values
        key1 = 'a'
        key2 = 'b'
        key3 = 3

        val1 = 1
        val2 = 2
        val3 = 'c'

        # Init hash table
        hash_table = hash_tables.HashTable()

        # Put key/val pairs in table
        hash_table.put(key1, val1)
        hash_table[key2] = val2
        hash_table[key3] = val3

        # Get values back
        ret1 = hash_table.get(key1)
        ret2 = hash_table[key2]
        ret3 = hash_table[key3]

        # Assert they are what was input
        err_msg = 'returned value: %s does not correspond to key: %s'
        self.assertEqual(ret1, val1, msg=err_msg % (str(ret1), key1))
        self.assertEqual(ret2, val2, msg=err_msg % (str(ret2), key2))
        self.assertEqual(ret3, val3, msg=err_msg % (str(ret3), key3))




if __name__ == '__main__':
    unittest.main()