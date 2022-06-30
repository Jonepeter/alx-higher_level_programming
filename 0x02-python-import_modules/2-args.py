#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    len_args = len(args) - 1
    if len_args > 1:
        print(len_args, 'arguments:')
        for i in range(1, len_args + 1):
            print('{:d}: {}'.format(i, args[i]))
    elif len_args == 1:
        print(len_args, 'argument:')
        for i in range(1, len_args + 1):
            print('{:d}: {}'.format(i, args[i]))
    elif len_args == 0:
        print(len_args, 'arguments.')

         


