#!/usr/bin/python3
"""Module.



"""


class BaseGeometry:
    """
    class
    """
    def area(self):
        """
        function that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True
