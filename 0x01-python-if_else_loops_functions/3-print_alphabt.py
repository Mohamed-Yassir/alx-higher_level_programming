#!/usr/bin/python3
for y in range(ord('a'), ord('z') + 1):
    if y != ord('q') and y != ord('e'):
        print("{:c}".format(y), end="")
