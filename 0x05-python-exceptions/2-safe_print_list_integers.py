#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints all integer elements of a list"""
    count = 0
    idx = 0
    while count < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            count += 1
            idx += 1
        except (ValueError, TypeError):
            idx += 1
            pass
        except IndexError:
            break
    print()
    return count
