# arrays_strings/strings.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''

def check_unique_chars(input_str):
    '''
    Function to check if string is composed of all unique characters

    Paramters
    ---------
    input_str : string
        input string to test for unique-ness

    Returns
    -------
    is_unique : boolean
        flag indicating whether string is unique or not
    '''

    # Import packages

    # Init variables
    chars_dict = {}
    is_unique = True

    # Iterate through string chars
    for char in input_str:
        if not chars_dict.has_key(char):
            chars_dict[char] = 1
        else:
            is_unique = False
            break

    # Return flag
    return is_unique