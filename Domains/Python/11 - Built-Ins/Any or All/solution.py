input()
Tarr = [[(i == i[::-1]), len(i) < 3 and i[0] != '-'] for i in input().split()]
print(any([i[0] for i in Tarr]) and all([i[1] for i in Tarr]))