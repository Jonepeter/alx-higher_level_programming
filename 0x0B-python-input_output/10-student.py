#!/usr/bin/python3
''' Module Input Output'''


class Student:
    """
    class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dict.
        """
        x = {}
        if attrs is not None:
            for i in attrs:
                if hasattr(self, i):
                    x[i] = self.__dict__[i]
            return x
        return self.__dict__
