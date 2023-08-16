#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns new dictionary values multiplied by 2"""
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
