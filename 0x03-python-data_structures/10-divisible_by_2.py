#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    inputlist = my_list[:]
    for sum_total, index in enumerate(my_list):
        if index % 2 == 0:
            inputlist[sum_total] = True
        else:
            inputlist[sum_total] = False
    return(inputlist)
