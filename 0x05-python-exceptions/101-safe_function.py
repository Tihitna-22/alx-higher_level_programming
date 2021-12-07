#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except IndexError as indexerr:
        print("Exception: {}".format(indexerr), file=sys.stderr)
        result = None
    except ZeroDivisionError as zeroerr:
        print("Exception: {}".format(zerroerr), file=sys.stderr)
        result = None
    return result
