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

# Calculates cumulative distribution of atleast 2 rejects
# (i.e. from 2 to batch quantity = 'batch' )
def cumulativeDistAtleast2(pDefective, pNonDefective, batch):
    cd = 0
    for i in range(2, batch+1):
        cd += c(batch, i) * (pDefective ** i) * (pNonDefective ** (batch-i))
    
    return cd

# Calculates cumulative distribution of atmost 2 rejects
# (i.e. from 0 to batch quantity = '2' )
def cumulativeDistAtmost2(pDefective, pNonDefective, batch):
    cd = 0
    for i in range(0, 3):
        cd += c(batch, i) * (pDefective ** i) * (pNonDefective ** (batch-i))
    
    return cd

if __name__ == '__main__':
    defectivePistonPerc, batch = map(int, input().split())

    pDefectivePiston = defectivePistonPerc/100
    pNonDefectivePiston = 1 - pDefectivePiston

    print(round(
        cumulativeDistAtmost2(pDefectivePiston, pNonDefectivePiston, batch),3))

    print(round(
        cumulativeDistAtleast2(pDefectivePiston, pNonDefectivePiston, batch), 3))