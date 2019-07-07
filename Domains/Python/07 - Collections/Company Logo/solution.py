import collections
import operator
import itertools

s = list(input())

sCount = collections.OrderedDict.fromkeys('abcdefghijklmnopqrstuvwxyz')

for key, val in sCount.items():
    sCount[key] = 0

for i in s:
    try:
        sCount[i] += 1
    except(IndexError):
        sCount[i] = 1

for i in range(3):
    ob = max(sCount.items(), key = operator.itemgetter(1))
    key = ob[0]
    value = ob[1]
    del sCount[key]
    print(str(key) + ' ' + str(value))
