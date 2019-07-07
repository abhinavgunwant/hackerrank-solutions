n, x = [int(i) for i in input().split()]
marks = [0.0 for i in range(n)]
for i in range(x):
    temp = [float(k) for k in input().split()]
    for j in range(n):
        marks[j] += temp[j]

print("\n".join(map(str, [i/x for i in marks])))