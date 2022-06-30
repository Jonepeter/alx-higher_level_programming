#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    len_args = len(args) - 1
    sum = 0
    if len_args > 1:
        for i in range(1, len_args + 1):
            sum += int(args[i])
    elif len_args == 1:
        for i in range(1, len_args + 1):
            sum += int(args[i])
    print(int(sum))
