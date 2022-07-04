#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        length = len(sentence)
        first_letter = sentence[0]
        return(length, first_letter)
    else:
        return(0, None)
