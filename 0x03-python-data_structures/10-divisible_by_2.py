#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # loop through the up to list length
    new_list = []
    for i in range(len(my_list)):
        # return true if it is divisible by 2
        if ((my_list[i] % 2) == 0):
            new_list.append(True)
        # return false if it is not divisible by 2
        elif ((my_list[i] % 2 )!= 2):
            new_list.append(False)
    return new_list
