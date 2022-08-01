#!/usr/bin/python3
"""Module.



"""


class MyInt(int):
    """
    subclass
    """
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
