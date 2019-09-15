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


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print(round(pearsonCorrCoeff(X, Y, n), 3))