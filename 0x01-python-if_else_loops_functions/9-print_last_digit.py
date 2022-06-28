#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
    else:
        last_digit = (abs(number) % 10)
    print("{0}".format(last_digit))
