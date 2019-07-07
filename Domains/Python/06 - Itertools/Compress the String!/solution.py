import itertools

m = list(input())

groups = itertools.groupby(m)
resList = []

for k, g in groups:
    resList.append([len(list(g)), k])

print(' '.join(['(' + ', '.join([str(j) for j in i]) + ')' for i in resList]))
