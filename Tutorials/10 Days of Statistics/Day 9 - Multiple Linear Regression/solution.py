import math
from sklearn import linear_model

m, n = map(int, input().split())
X = []
Y = []

for i in range(n):
    inp = list(map(float, input().split()))
    X.append(inp[0:-1])
    Y.append(inp[-1])

qNo = int(input())

query = []

for i in range(qNo):
    query.append(list(map(float, input().split())))

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for q in query:
    bx = 0

    for i in range(m):
        bx += b[i] * q[i]

    print(a + bx)