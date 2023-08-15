#!/usr/bin/python3

def divisibe_by_2(my_list=[]):
    new_list = ""

    for num in my_list:
        if num % 2 == 0:
            new_list += True
        else:
            new_list += False
    return new_list
