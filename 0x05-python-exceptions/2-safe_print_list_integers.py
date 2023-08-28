#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Function prints first x elements of a list that are integers.

    Args:
        my_list (list): Refers to list to print elements from.
        x (int): Amount of elements to print.

    Returns:
        Printed amount of elements.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
