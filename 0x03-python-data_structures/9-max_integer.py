#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    if(len(my_list) != 0):
        for i in my_list:
            if(i >= large):
                large = i;
    else:
        return None
    return large
