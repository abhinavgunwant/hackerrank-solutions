n = int(input())
arr = [int(i) for i in input().split()]

arr.sort()

highest = -1

for i in reversed(arr):
    if i != highest and highest != -1:
        print(i)
        break
    highest = i