# pytools/recursion/json_parse.py
#
# Author: Daniel Clark, 2016

'''
This module contains a function to parse a json object to find and replace
string values
'''


def json_parse(json, key_str, old_str, new_str):
    '''

    :param json:
    :param key_str:
    :param old_str:
    :param new_str:
    :return:
    '''

    if isinstance(json, int):
        return None
    if isinstance(json, str):
        if json != old_str:
            return None
        else:
            return new_str
    if isinstance(json, list):
        for i, el in enumerate(json):
            val = json_parse(el, key_str, old_str, new_str)
            if val:
                json[i] = val
                return json
        return None
    if isinstance(json, dict):
        if key_str != '':
            keys = key_str.split('.')
            key = keys.pop(0)
            key_str = '.'.join(keys)
        if key in json:
            val = json_parse(json[key], key_str, old_str, new_str)
            if val:
                json[key] = val
        elif json.has_key(old_str):
            json[old_str] = new_str
            return json
        else:
            return None
