n1 = int(input())
s1 = set([int(i) for i in input().split()])
n2 = int(input())
s2 = set([int(i) for i in input().split()])

s1is2 = s1.intersection(s2)
s1us2 = s1.union(s2)

symDiff = s1us2 - s1is2
symList = list(symDiff)
symList.sort()

for i in symList:
    print(i)