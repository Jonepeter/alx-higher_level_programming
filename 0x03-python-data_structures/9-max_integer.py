#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    for i in my_list:
        if(my_list[i].isdigit() == True):
            if(my_list[i] > large):
                large = my_list[i];
        else:
            return None
    return large