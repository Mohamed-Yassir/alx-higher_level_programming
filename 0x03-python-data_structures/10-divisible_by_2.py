#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdi = []
    for i in my_list:
        if (i % 2) == 0:
            listdi.append(True)
        else:
            listdi.append(False)
    return listdi
