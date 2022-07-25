#!/usr/bin/python3
"""A square is a rectangle"""


class Rectangle:
    """ Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            for i in range(self.__width):
                s += str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
