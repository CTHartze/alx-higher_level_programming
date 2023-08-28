#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Function executed safely.

    Args:
        fct: Refers to function to execute.
        args: fct arguments.

    Returns:
        Function result,
        None - when error occurs.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
