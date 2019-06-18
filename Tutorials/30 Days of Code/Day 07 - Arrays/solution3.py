#!/bin/python3

# Note: This solution takes a simpler approach, refer
# solution2.py and solution3.py for more 'Pythonic'
# solutions!

import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(input().rstrip().split())
    arr.reverse()

    print(' '.join(arr))