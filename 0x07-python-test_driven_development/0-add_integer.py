#!/usr/bin/python3

def add_integer(a, b=98):
    data_types = (int, float)
    if not isinstance(a, data_types):
        raise TypeError("a must be an integer")
    if not isinstance(b, data_types):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
