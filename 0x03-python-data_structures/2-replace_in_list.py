#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
        Function that replaces an element of specific idx with new element
        
        If idx is negative, the function should not modify anything, 
        and returns the original list
        If idx is out of range (> of number of element in my_list), 
        the function should not modify anything, and returns the original list
    '''
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
