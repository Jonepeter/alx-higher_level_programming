#!/usr/bin/python3
"""Module.


"""


def print_stat(s, d):
    """
    print the stats and size.
    """
    try:
        print("File size: {}".format(s))
        for k, v in sorted(d.items()):
            if v != 0:
                print("{}: {}".format(k, v))
    except Exception:
        pass
