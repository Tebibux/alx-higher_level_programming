#!/usr/bin/python3
def weight_average(my_list=[]):
    upperNumber = 0
    lowerNumber = 0
    if my_list == '':
        return (0)
    else:
        for numbersInTuple in my_list:
            upperNumber += numbersInTuple[0] * numbersInTuple[1]
            lowerNumber += numbersInTuple[1]
    return upperNumber/lowerNumber
