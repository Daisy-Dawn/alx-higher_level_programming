#!/usr/bin/python3

def common_elements(set_1, set_2):
    my_elements = set()
    for items in set_1:
        if items in set_2:
            my_elements.add(items)
    return my_elements
