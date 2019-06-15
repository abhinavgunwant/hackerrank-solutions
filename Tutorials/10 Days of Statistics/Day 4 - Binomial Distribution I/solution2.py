#!/bin/python3

import math
import functools

def factorial(n):
    if n > 1:
        return functools.reduce(lambda a, b: a * b, range(n, 1, -1))
    
    return 1

def c(n, r):
    return factorial(n)/(factorial(r) * factorial(n-r))


def calcSolution(pb, pg):
    solution = 0
    for i in range(3, 7):
        solution += c(6, i) * (pb ** i) * (pg ** (6-i))
    
    return solution


if __name__ == '__main__':
    b, g = list(map(float, input().split()))

    probBoy = b/(1+b)
    probGirl = 1 - probBoy

    print(round(calcSolution(probBoy, probGirl), 3))