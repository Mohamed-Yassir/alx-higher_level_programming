#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    integer = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file = sys.stderr)
        integer = False
    return integer
