#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_list = list(a_dictionary.keys())
    new_dic = a_dictionary.copy()
    for value in dic_list:
        new_dic[value] *= 2
    return new_dic
