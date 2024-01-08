#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    init_list = my_list[:]
    if 0 <= idx < len(my_list):

        init_list[idx] = element
        return(init_list)
    return(my_list)
