#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return ("None")
    _input = my_list[0]
    for index in my_list:
        if index > _input:
            _input = index
    return (_input)
