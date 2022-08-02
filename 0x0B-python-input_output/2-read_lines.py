#!/usr/bin/python3
"""Module.



"""


def read_lines(filename="", nb=0):
    """
    function
    """
    with open(filename, encoding="utf-8") as f:
        if nb <= 0:
            print(f.read(), end="")
            return

        for i, line in enumerate(f):
            if i != nb:
                print(line, end="")
            else:
                return
