import collections

n = int(input())

word = list()
wOrdered = collections.OrderedDict()

for i in range(n):
    inp = input()
    try:    
        wOrdered[inp] += 1
    except(KeyError):
        wOrdered[inp] = 1
        
print(len(wOrdered))

print(' '.join(list(map(str, wOrdered.values()))))