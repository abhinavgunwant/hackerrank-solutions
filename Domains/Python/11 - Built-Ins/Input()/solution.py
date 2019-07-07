import re
x, k = [int(i) for i in input().split()]

poly = input()

terms = re.split('\s*[+-]\s*', poly)

sign = []

signs = ['+', '-']

for i in poly:
    if i in signs:
        if i == '+':
            sign.append(1)
        else:
            sign.append(-1)


sign.reverse()

sign.append(1)
res = 0

for i in terms:
    if bool(re.match(r'x\*\*\d+', i)):
        tmp = i.split('**')
        res += sign.pop() *( x ** int(tmp[1]))
    elif bool(re.match(r'x\*\d+', i)):
        tmp = i.split('*')
        res += sign.pop() * (x * int(tmp[1]))
    elif bool(re.match(r'\d+\*x\*\*\d+', i)):
        tmp = i.split('*x**')
        res += sign.pop() * (int(tmp[0]) * (x ** int(tmp[1])))
    else:
        if i == 'x':
            res += sign.pop() * (x)
        elif i.isdigit():
            res += sign.pop() * (int(i))

if res == k:
    print(True)
else:
    print(False)
