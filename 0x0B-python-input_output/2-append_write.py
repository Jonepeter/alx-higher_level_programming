#!/usr/bin/python3
''' Module Input Output'''


def append_write(filename="", text=""):
    ''' Append  write'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
