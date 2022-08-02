#!/usr/bin/python3
"""Module number_of_lines"""


def number_of_lines(filename=""):
    """ function number_of_lines """
    x = 0
    with open(filename) as f:
        return len(list(f))
