import itertools

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(' '.join([str(i) for i in list(itertools.product(A,B))]))