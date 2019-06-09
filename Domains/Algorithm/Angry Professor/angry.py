#!/bin/python

import sys

ans = []

def calc(curr_t, n, k, a):
    stuInClass = 0
    for i in range(n):
        if(a[i] <= 0):
            stuInClass += 1


    if(stuInClass >= k):
        ans.append("NO")
    else:
        ans.append("YES")



t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    calc(a0, n, k, a)

lim = len(ans)
for i in range(lim):
    print(ans[i])
