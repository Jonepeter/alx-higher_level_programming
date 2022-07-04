#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list)
    for i in reversed(range(0,le)):
        print(my_list[i])
