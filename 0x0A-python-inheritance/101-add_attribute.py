#!/usr/bin/python3
"""Module.



"""


def add_attribute(obj, attr, value):
    """
    adds attribute if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
