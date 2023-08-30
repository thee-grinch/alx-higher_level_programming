#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """runs a function safely"""
    try:
        func = fct(*args)
        return func
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
