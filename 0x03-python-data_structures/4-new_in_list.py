#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mynew_list = my_list[:]
    if 0 <= idx < len(mynew_list):
        mynew_list[idx] = element
        return (mynew_list)
