n, m = [int(i) for i in input().split()]
k = 0
table = list()

for i in range(n):
    table.append(list(map(int, input().split())))

k = int(input())

table = sorted(table, key = lambda l:l[k])

for i in table[:]:
    print(' '.join(list(map(str, i))))