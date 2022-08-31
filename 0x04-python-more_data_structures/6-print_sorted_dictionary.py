#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orderOfList = list(a_dictionary.keys())
    orderOfList.sort()
    for i in orderOfList:
        print("{}: {}".format(i, a_dictionary.get(i)))
