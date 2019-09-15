n = input()
A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    cmd = input().split()[0]
    X = set(map(int, input().split()))
    
    if cmd == 'intersection_update':
        A.intersection_update(X)
    elif cmd == 'update':
        A.update(X)
    elif cmd == 'difference_update':
        A.difference_update(X)
    elif cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(X)
    
print(sum(A))