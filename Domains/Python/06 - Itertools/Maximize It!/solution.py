import itertools

def f(x):
    return x * x

k, m = map(int, input().split())

K = []

for i in range(k):
    K.append(list(map(int, input().split()))[1:])

paramList = list(itertools.product(*K))

Smax = -1

for param in paramList:
    S = 0

    for param_ in param:
        S += f(param_)

    S %= m

    if S > Smax:
        Smax = S

print(Smax)
