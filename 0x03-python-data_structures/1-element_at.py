#!/usr/bin/python3
def element_at(my_list, idx):
    '''
        Function that returns the element at the given index
        
        If idx is negative, the function should return None
        If idx is out of range (> of number of element in my_list), the function should return None
    '''
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
