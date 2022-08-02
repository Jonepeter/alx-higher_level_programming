#!/usr/bin/python3
''' Module Input Output'''


def pascal_triangle(n):
    """
    function.
    """
    l = []
    if n <= 0:
        return l
    if n == 1:
        return [[1]]
    r = [[1] for i in range(n)]
    for i in range(n):
        for j in range(i):
            x = 0
            if j != i - 1:
                x = r[i - 1][j] + r[i - 1][j + 1]
                r[i].append(x)
            else:
                r[i].append(1)
    return r
