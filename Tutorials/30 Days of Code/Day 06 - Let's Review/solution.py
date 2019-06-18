#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input())

    strings = []

    for i in range(n):
        strings.append(input())
    
    for string in strings:
        for oddCharIndex in range(0, len(string), 2):
            sys.stdout.write(string[oddCharIndex])

        sys.stdout.write(' ')

        for evenCharIndex in range(1, len(string), 2):
            sys.stdout.write(string[evenCharIndex])

        sys.stdout.write('\n')