#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    iteration = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end='')
        except:
            break
        else:
            iteration +=
    print()
    return (iteration)
