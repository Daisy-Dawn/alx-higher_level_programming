#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    empty = ()
    empty2 = tuple_a + (0, 0)
    empty3 = tuple_b + (0, 0)
    empty = empty2[0] + empty3[0], empty2[1] + empty3[1]
    return empty
