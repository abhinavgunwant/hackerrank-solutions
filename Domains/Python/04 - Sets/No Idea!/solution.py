n,m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    
    elif i in B:
        happiness -= 1
        
print(happiness)