#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqList = []
    sum = 0
    for item in my_list:
        if item not in uniqList:
            uniqList.append(item)
    for i in uniqList:
        sum += i
    return sum
