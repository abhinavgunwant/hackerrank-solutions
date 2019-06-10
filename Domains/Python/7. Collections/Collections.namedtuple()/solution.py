import collections

n = int(input())
cols = input()

Marks = collections.namedtuple('Marks', cols)
marksheet = []

for i in range(n):
    inp = input().split()
    marksheet.append(Marks(inp[0], inp[1], inp[2], inp[3]))
    
avg = 0

for i in marksheet:
    avg += float(i.MARKS)
    
avg /= n

print(round(avg, 2))