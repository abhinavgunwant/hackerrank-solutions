#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

noOfSteps = 0

####  Bubble sort
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

            noOfSteps += 1

print('Array is sorted in ' + str(noOfSteps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))