#!/usr/bin/python3

def no_c(my_string):
    i = ''
    for x in my_string:
        if x.upper() != 'C':
            i += x
    return i
