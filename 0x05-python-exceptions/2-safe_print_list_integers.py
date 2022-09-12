#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iterator = 0

    for num in range(x):
        try:
            print("{:d}".format(my_list=[num]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            iterator += 1
    print()
    return (iterator)
