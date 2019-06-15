#!/bin/python3

import math

def factorial(n):
    fact = 1

    while n > 1:
        fact *= n
        n -= 1
    
    return fact

# Calculates combination
def c(n, r):
    return factorial(n)/(factorial(r) * factorial(n-r))

# Calculates cumulative distribution of min 3 and max
# 6 boys in a family of 6.
# pb = probability that the child is a boy
# pg = probability that the child is a girl
def cumulativeDistribution(pb, pg):
    solution = 0
    for i in range(3, 7):
        solution += c(6, i) * (pb ** i) * (pg ** (6-i))
    
    return solution

if __name__ == '__main__':
    # Inputs are in the form of odds (boys:girls)
    b, g = list(map(float, input().split()))

    # Convert odds into probability
    probBoy = b/(1+b)               # P(boy)
    probGirl = 1 - probBoy          # P(girl)

    print(round(cumulativeDistribution(probBoy, probGirl), 3))