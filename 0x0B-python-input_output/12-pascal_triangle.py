#!/usr/bin/python3
''' Moduae Input Output'''


def pascal_triangle(n):
    """
    function.
    """
    a = []
    if n <= 0:
        return a
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
