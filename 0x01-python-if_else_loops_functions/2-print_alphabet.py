#!/usr/bin/python3
letter_in_ASCII = 97
while letter_in_ASCII < 123:
    str1 = chr(letter_in_ASCII)
    print("{}" .format(str1), end='')
    letter_in_ASCII += 1
