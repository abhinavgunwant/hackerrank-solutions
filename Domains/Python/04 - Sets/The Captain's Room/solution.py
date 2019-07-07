k = int(input())
rooms = [int(i) for i in input().split()]
x = dict()
for i in rooms:
    if i not in x:
        x[i] = 1
    else:
        x[i] += 1
        
for key,value in x.items():
    if value != k:
        print(key)
        break