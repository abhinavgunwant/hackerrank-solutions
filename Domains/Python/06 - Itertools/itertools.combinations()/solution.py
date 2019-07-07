import itertools

m,n = input().split()
n = int(n)
cList = list()

for k in range(1, n+1):
    tempList = list(itertools.combinations(list(m), k))
    for i in range(len(tempList)):
        tempList[i] = list(tempList[i])
        tempList[i].sort()        
    tempList.sort()
    cList += tempList
    
for i in cList:
    temp = list(i)
    temp.sort()
    print(''.join(temp))