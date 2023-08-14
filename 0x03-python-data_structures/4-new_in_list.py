#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """
    Replace element in list at specific position
    without modifying the original list.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
