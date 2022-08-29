#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        for i in range(len(my_list)):
            for j in range(0, len(my_list) - i -1):
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
        return my_list[-1]
