#!/usr/bin/python3


def search_replace(my_list, search, replace):
    temp_list = []

    for item in my_list:
        if item == search:
            item = replace
        temp_list.append(item)

    return(temp_list)
