#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is []:
        return 0
    total = 0
    no = 0
    for tup in my_list:
        total += tup[0] * tup[1]
        no += tup[1]
    return total / no
