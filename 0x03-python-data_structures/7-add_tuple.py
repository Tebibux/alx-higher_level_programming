#!/usr/bin/python3
def add_tuple(tuple1, tuple2):
    t_1_len = len(tupel1)
    t_2_len = len(tupel2)

    if t_1_len == 0:
        a1 = 0
        a2 = 0
    elif t_1_len == 1:
        a1 = tupel1[0]
        a2 = 0
    else:
        a1 = tupel1[0]
        a2 = tupel1[1]

    if t_2_len == 0:
        b1 = 0
        b2 = 0
    elif t_2_len == 1:
        b1 = tupel2[0]
        b2 = 0
    else:
        b1 = tupel2[0]
        b2 = tupel2[1]

    new_tuple = (a1 + b1, a2 + b2)

    return (new_tuple)
