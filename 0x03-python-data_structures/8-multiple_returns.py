#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    z = ()
    if x == 0:
        z = 0, "None"
    else:
        z = x, y
    return z
