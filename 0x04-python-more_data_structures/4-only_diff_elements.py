#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newSet = []
    for item in set_1:
        if item not in set_2:
            newSet.append(item)
    for item2 in set_2:
        if item2 not in set_1:
            newSet.append(item2)
    return newSet
