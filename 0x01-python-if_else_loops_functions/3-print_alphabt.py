#!/usr/bin/python3
for alphabet_letter in range(ord('a'), ord('z') + 1):
    if chr(alphabet_letter) != 'e' and chr(alphabet_letter) != 'q':
        print('{:c}'.format(alphabet_letter), end='')
