#!/usr/bin/pyhton3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_copy = my_list.copy()
    list_copt.sort()
    return list_copy[-1]
