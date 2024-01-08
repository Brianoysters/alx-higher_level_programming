#!/usr/bin/python3
def multiple_returns(sentence):

    size = len(sentence)
    first_character = sentence[0] if size > 0 else "None"
    output = size, first_character
    return(output)
