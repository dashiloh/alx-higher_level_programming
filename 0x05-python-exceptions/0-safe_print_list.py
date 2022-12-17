#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_no = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_no += 1
        except IndexError:
            break
    print()
    return printed_no
