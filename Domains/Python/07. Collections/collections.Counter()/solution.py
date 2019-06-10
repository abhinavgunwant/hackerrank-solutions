import collections

balance = 0
x = int(input())
s_sizes = collections.Counter(list(map(int, input().split())))

for i in range(int(input())):
    size, price = list(map(int, input().split()))
    if size in s_sizes.keys() and s_sizes[size] > 0:
        s_sizes[size] -= 1
        balance += price

print(balance)