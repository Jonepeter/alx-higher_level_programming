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
        if type(attrs) is list and all([isinstance(x, str) for x in attrs]):
            for i in attrs:
                if hasattr(self, i):
                    x[i] = str(getattr(self, i))
            return x
        return self.__dict__

    def reload_from_json(self, json):
        """
        function.
        """
        for i, j in json.items():
            setattr(self, i, j)
