#!/usr/bin/python3

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coorList = [i for i in range(n)]

xList = [i for i in range(x+1)]
yList = [i for i in range(y+1)]
zList = [i for i in range(z+1)]

res = [[i,j,k] for i in xList for j in yList for k in zList if i+j+k != n]

res.sort()
print(res)