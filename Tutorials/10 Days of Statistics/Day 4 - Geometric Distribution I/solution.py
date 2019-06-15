#!/bin/python3

# Calculates the grometric distribution .Refer to the hackerrank
# tutorial page of this problem (link to the tutorial can also be
# found in urls.txt file of this folder!)
def geometricDist(p, n):
    return (p) * ((1 - p) ** (n - 1))

if __name__ == '__main__':
    defectiveNumerator, defectiveDenominator = map(int, input().split())
    n = int(input())

    defectiveProbability = defectiveNumerator / defectiveDenominator

    print(round(geometricDist(defectiveProbability, n), 3))