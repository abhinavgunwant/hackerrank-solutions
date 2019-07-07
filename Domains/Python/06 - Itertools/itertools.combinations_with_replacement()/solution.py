import itertools
m,n = input().split()
n = int(n)
cList = list(itertools.combinations_with_replacement(m, n))
for i in range(len(cList)):
    cList[i] = list(cList[i])
    cList[i].sort()
cList.sort()
for i in cList:
    print(''.join(i))