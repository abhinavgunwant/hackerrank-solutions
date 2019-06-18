#!/bin/python3

# A more 'pythonic' solution!

import itertools

if __name__ == '__main__':
    # Get binary string for the input decimal integer
    binStr = bin(int(input()))

    # Get the length of consecutive 1's in list
    # (with length of 0's as 0 so that it's not)
    consec1 = [len(list(g)) if k == '1' else 0 for k, g in itertools.groupby(binStr)]

    print(max(consec1))