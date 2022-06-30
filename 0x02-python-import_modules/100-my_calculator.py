#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    len_args = len(argv) - 1
    
    if len_args == 3:
        num1 = int(argv[1])
        num2 = int(argv[3])
        operator = argv[2]
        if (operator == '+'):
            print("{:d} {} {:d} = {:d}".format(num1, operator, num2, add(num1, num2)))
            exit(0)
        elif (operator == '-'):
            print("{} {} {} = {:d}".format(num1, operator, num2, sub(num1, num2)))
            exit(0)
        elif (operator == '*'):
            print("{} {} {} = {:d}".format(num1, operator, num2, mul(num1, num2)))
            exit(0)
        elif (operator == '/'):
            print("{} {} {} = {:d}".format(num1, operator, num2, int(div(num1, num2))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
