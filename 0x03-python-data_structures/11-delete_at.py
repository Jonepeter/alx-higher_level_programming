#!/usr/bin/python3
from re import M


def delete_at(my_list=[], idx=0):
    # if idx is negative or out of range, nothing change (returns the same list)
    new_list = []
    leng = len(my_list) - 1
    if idx >= 0 and idx <= leng:
        for i in my_list:
            if i != my_list[idx]:
                new_list.append(i)
        return new_list
    else:
        return new_list
