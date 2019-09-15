import operator
import functools

def sortFunc(a):
    key = 0
    if a.islower():
        return ord(a) - 97
    
    if a.isupper():
        return ord(a) - 65 + 30
    
    if a.isdigit():
        if int(a) % 2 == 0:
            return ord(a) + 200
    return ord(a) + 100

print(functools.reduce(operator.add, sorted(input(), key=sortFunc)))