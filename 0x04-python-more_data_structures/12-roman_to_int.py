#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        current = roman.get(roman_string[i])
        if i != len(roman_string) - 1:
            Next = roman.get(roman_string[i + 1])
        else:
            Next = 0
        if current >= Next:
            total += current
        else:
            total += Next - current
            i += 2
    return total
