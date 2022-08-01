#!/usr/bin/python3
"""Module



"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclass
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
