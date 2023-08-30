#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """safely prints an int"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError, OverflowError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
