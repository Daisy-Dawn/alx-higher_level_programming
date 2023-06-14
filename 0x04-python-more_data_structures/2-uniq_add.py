#!/usr/bin/python3

def uniq_add(my_list=[]):
    summ = 0
    new_list = set()
    for num in my_list:
        if num not in new_list:
            summ += num
            new_list.add(num)
    return summ
