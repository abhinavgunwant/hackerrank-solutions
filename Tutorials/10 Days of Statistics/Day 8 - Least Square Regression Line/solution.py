import math

def mean(l):
    return sum(l) / len(l)

def stdDeviation(l):
    n = len(l)
    mean_ = mean(l)
    var = 0

    for i in range(n):
        var += (mean_ - l[i]) ** 2

    var /= n

    return math.sqrt(var)


def cov(X, Y):
    xMean = mean(X)
    yMean = mean(Y)
    n = len(X)
    covar = 0

    for i in range(n):
        covar += (X[i] - xMean) * (Y[i] - yMean)

    covar /= n

    return covar


def pearsonCorrCoeff(X, Y, n):
    return cov(X, Y) / (stdDeviation(X) * stdDeviation(Y))

X = []
Y = []
n = 5

for i in range(n):
    x, y = list(map(float, input().split()))

    X.append(x)
    Y.append(y)

b = pearsonCorrCoeff(X, Y, n) * stdDeviation(Y) / stdDeviation(X)
a = mean(Y) - b * mean(X)

x = 80

y = a + b * x

print(round(y, 3))