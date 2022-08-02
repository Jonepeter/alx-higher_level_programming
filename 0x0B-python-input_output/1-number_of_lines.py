#!/usr/bin/python3
"""Module.



"""


def number_of_lines(filename=""):
    """
    function.
    """
    x = 0
    with open(filename) as f:
        return len(list(f))
