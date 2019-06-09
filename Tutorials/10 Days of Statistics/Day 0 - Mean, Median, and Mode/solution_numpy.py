#### Note: This example uses numpy! It would be better to
#### consider the solution.py example for learning
#### perspective. This example here is to demonstrate
#### the ease with which programs can be written using
#### numpy...

import numpy
from scipy import stats

n = int(input())

xArr = [int(i) for i in input().split()]

X = numpy.array(xArr)

print(numpy.mean(X))
print(numpy.median(X))
print(stats.mode(X).mode[0])