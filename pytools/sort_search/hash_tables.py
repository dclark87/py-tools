# pytools/sort_search/hash_tables.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''


class HashTable(object):
    '''
    Implement a hash table that stores key/value pairs and provides
    O(1) time access
    '''

    def __init__(self, size=11):
        '''
        Init HashTable object
        '''

        self.size = size
        self.key_slots = [None] * size
        self.val_slots = [None] * size

    def _hash_function(self, key):
        '''
        Hashing function to convert key into slot index
        '''

        # Check key type
        if isinstance(key, str) and len(key) == 1:
            key = ord(key)
        elif not isinstance(key, int):
            err_msg = 'Key: %s must be a char or int type!' % str(key)
            raise KeyError(err_msg)

        hash_index = key % self.size
        return hash_index

    def _rehash_function(self, hash_index):
        '''
        Re-hash function to incrementally move initial index if
        slot at original index is full
        '''

        new_index = (hash_index+1)%self.size
        return new_index

    def put(self, key, value):
        '''
        Put key/value pair into hash table
        '''

        # Get the hash index
        orig_hash_index = self._hash_function(key)
        hash_index = orig_hash_index

        # While the slot is filled and containing another key
        while self.key_slots[hash_index] != None and \
            self.key_slots[hash_index] != key:

            # Get rehashed index
            hash_index = self._rehash_function(hash_index)

            # If we've gone all the way around
            if hash_index == orig_hash_index:
                err_msg = 'Key: %s cannot find unique slot, try increasing '\
                          'hash table size or using a different key'
                raise KeyError(err_msg)

        # Update key and val slots with key/val pair
        self.key_slots[hash_index] = key
        self.val_slots[hash_index] = value

    def get(self, key):
        '''
        Get value from key
        '''

        # Get first hash_index
        orig_hash_index = self._hash_function(key)
        hash_index = orig_hash_index

        # While key is not found, rehash
        while self.key_slots[hash_index] != key:
            hash_index = self._rehash_function(hash_index)

            if hash_index == orig_hash_index:
                err_msg = 'Key: %s not located in hash table!' % key
                raise KeyError(err_msg)

        return self.val_slots[hash_index]

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)