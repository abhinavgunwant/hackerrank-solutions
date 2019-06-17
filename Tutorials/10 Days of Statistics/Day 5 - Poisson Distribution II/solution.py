#!/bin/python3

def dialyOperatingCostA(x):
    l = (160) + (40 * (x + x*x))
    return l

def dailyOperatingCostB(y):
    l = (128) + (40 * (y + y*y))
    return l

if __name__ == '__main__':
    X, Y = map(float, input().split())

    print(round(dialyOperatingCostA(X), 3))
    print(round(dailyOperatingCostB(Y), 3))