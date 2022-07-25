#!/usr/bin/python3
''' Getting Rectangle height and width'''


class Rectangle:
    ''' A rectangle module'''

    def __init__(self, width=0, height=0):
        ''' Initializes a new Rectangle object'''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' get and set the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = int(width)

    @property
    def height(self):
        '''get and set the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = int(height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
