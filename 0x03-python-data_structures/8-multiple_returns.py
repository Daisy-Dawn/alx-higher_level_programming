#!/usr/bin/python3

def multiple_returns(sentence):
    z = ()
    if len(sentence) == 0:
        z = 0, "None"
    else:
        z = len(sentence), sentence[0]
    return z
