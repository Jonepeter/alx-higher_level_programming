#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    leng = len(my_list) - 1
    if idx >= 0 and idx <= leng:
        del my_list[idx]
        return my_list
    else:
        return my_list
