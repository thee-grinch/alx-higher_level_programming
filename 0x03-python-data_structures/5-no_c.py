#!/usr/bin/python3

def no_c(my_string):
    for char in my_string:
        if char == "c":
            my_string.remove("c")
        if char == "C":
            my_string.remove("C")
            
    return my_string
