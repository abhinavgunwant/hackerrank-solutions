#!/bin/python3

import math
import os
import random
import re
import sys

def solve(str_):
    s = str_[0].upper()
    space = False
    for i in str_[1:]:
        if space and i != ' ':
            s += i.upper()
            space = False
            continue
            
        if i == ' ':
            space = True
        
        s += i
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()