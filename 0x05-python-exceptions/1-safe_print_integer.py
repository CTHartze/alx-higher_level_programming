#!/usr/bin/python3

def safe_print_integer(value):
    """Integer printed in "{:d}".format().

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
        return (False)
