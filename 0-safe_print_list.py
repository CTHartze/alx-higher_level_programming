#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function prints x list elements.

    Args:
        my_list (list): Refers to list to prints elements from.
        x (int): Refers to amount of elements to print.

    Returns:
        Printed amount of elements.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
