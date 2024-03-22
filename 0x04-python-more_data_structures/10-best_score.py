#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxv = 0
    keyv = None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxv = v
            keyv = k
    return keyv
