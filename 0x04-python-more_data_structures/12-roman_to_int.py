#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    input_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [input_dict[x] for x in roman_string] + [0]
    roman_val = 0

    for index in range(len(numbers) - 1):
        if numbers[index] >= numbers[index+1]:
            roman_val += numbers[index]
        else:
            roman_val -= numbers[index]

    return roman_val
