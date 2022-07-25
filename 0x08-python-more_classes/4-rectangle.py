#!/usr/bin/python3
'''Print String using __str__ and __repr__'''


class Rectangle:
    """Defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """ """
        self.width = width
        self.height = height

    def __str__(self):
        s = ""
        for i in range(self.__height):
            for i in range(self.__width):
                s += "#"
            s += "\n"
        return s[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        function returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        function that returns the perimeter of the rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return 2 * (self.__width + self.__height)
