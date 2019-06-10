import collections
import sys

n,m = [int(i) for i in input().split()]

a = collections.defaultdict(list)
b = list()
for i in range(n):
    a[input()].append(i+1)

for i in range(m):
    b.append(input())
    
keys = list(a.keys())
#b = list(collections.OrderedSet(b))
firstLine = False
for i in b:
    if firstLine:
        sys.stdout.write("\n")
    if i not in keys:
        sys.stdout.write(str(-1))
    else:
        #' '.join(a[i])
        first = False
        for j in a[i]:
            if first:
                sys.stdout.write(' ')
            sys.stdout.write(str(j))
            first = True
    firstLine = True
    