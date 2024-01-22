#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    current_list = []
    for index in range(0, list_length):
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            current_list.append(quotient)
    return (current_list)
