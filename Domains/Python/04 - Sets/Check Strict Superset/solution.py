A = set(map(int, input().split()))
l = []
for i in range(int(input())):
    temp = set(map(int, input().split()))
    if not (temp.issubset(A) and len(A-temp) > 0):
        print('False')
        exit()

print('True')