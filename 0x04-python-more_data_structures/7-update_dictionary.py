#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary.keys():
        if keys == key:
            a_dictionary.update({key: value})
    return a_dictionary
