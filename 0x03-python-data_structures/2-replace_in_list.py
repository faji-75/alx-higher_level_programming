#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < (len(my_list)) and idx >= 0:
        my_list[idx] = element
        new_list = my_list
        return new_list
    else:
        return None
