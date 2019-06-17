#!/bin/python3

# Calculates factorial
def fact(n):
    f = 1
    while n > 0:        
        f *= n
        n -= 1
    
    return f

# Calculates Poisson Distribution
def poissonDist(k, l):
    return (l**k*(2.71828**(-l)))/fact(k)

if __name__ == '__main__':
    x = float(input())
    y = float(input())

    print(round(poissonDist(y, x), 3))