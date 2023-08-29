#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Attempts to divide a list"""
    idx = 0
    new_list = []
    div = 0
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            div = num1 / num2
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
