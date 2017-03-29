#!/usr/bin/env python
def shift(input, left, right):
    if len(input) == 1:
        return input
    return input[left:] + input[0:left]
    return input[-right:] + input[0:-right]

print shift("A", 0, 0)
