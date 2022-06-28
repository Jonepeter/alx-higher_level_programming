#!/usr/bin/python3
import dis
def myfunc(alist):
    return len(alist)

print(dis.dis(myfunc))