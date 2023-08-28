#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Function prints integer according to criteria.

    Args:
        value (int): Refers to integer to print.

    Returns:
        False when TypeError or ValueError occurs,
        else true.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
