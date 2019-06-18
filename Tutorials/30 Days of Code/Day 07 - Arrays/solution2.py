#!/bin/python3

# Note: This solution takes a simpler approach, refer
# solution2.py and solution3.py for more 'Pythonic'
# solutions!

import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n-1, -1, -1):
        sys.stdout.write(str(arr[i]))

        if i > 0:
            sys.stdout.write(' ')

        i -= 1