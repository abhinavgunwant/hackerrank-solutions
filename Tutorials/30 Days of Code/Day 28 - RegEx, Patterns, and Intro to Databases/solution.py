#!/bin/python3

import re

Names = []

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstName, emailID = input().split()

        if bool(re.match(r'^.*@gmail\.com', emailID)):
            Names.append([firstName, emailID])

        Names.sort()

    for name in Names:
        print(name[0])