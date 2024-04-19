#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    y, c = 0, 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end='')
            c += 1
        except (ValueError, TypeError):
            pass
        y += 1
    print()
    return c
