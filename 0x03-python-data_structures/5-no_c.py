#!/usr/bin/python3
def no_c(my_string):
    noc = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'C' or my_string[i] != 'c'):
            noc += my_string[i]
    return noc
