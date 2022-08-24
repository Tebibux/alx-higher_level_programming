#!/usr/bin/python3
def remove_char_at(str, indx_removed):
    updated_str = ""
    for i in range(len(str)):
        if i != indx_removed:
            updated_str = updated_str + str[i]
    return (updated_str)
