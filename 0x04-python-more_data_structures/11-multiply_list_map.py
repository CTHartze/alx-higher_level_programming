#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns list value multiplied by number, no loop"""
    return (list(map((lambda i: i * number), my_list)))
