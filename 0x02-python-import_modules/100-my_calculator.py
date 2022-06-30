#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    args = sys.argv
    len_args = len(args) - 1
    if len_args == 3:
        if (args[2] == '+'):
            print("{} {} {} = {:d}".format(args[1], args[2], args[3], add(int(args[1]), int(args[3]))))
        elif (args[2] == '-'):
            print("{} {} {} = {:d}".format(args[1], args[2], args[3], sub(int(args[1]), int(args[3]))))
        elif (args[2] == '*'):
            print("{} {} {} = {:d}".format(args[1], args[2], args[3], mul(int(args[1]), int(args[3]))))
        elif (args[2] == '/'):
            print("{} {} {} = {:d}".format(args[1], args[2], args[3], int(div(int(args[1]), int(args[3])))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
