#!/bin/python3

# Calculates the cumulative geometric distribution of
# the probability 'p' in first 'n' trials
def calcCumulativeGeometricDist(p, n):
    cgd = 0

    for i in range(1, n+1):
        cgd += (p) * ((1 - p) ** (i - 1))

    return cgd

if __name__ == '__main__':
    defectiveNumerator, defectiveDenominator = map(int, input().split())
    n = int(input())

    defectiveProbability = defectiveNumerator / defectiveDenominator

    print(round(calcCumulativeGeometricDist(defectiveProbability, n), 3))