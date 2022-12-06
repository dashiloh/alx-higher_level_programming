#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    total = 0
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    for i in unique_list:
        total += i
    return total
