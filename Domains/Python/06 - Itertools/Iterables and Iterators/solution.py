import itertools

n = int(input())
l = list(map(str, input().split()))
k = int(input())

comL = list(itertools.combinations(l, k))

total = len(comL)

noOfA = 0

for i in comL:
    if 'a' in i:
        noOfA += 1
        
print(noOfA/total)