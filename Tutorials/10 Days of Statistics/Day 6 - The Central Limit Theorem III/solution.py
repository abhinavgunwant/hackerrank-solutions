import math

def cumulativeDist(x, sigma, z):
    return z * sigma / ( math.sqrt(x) )

sampleValues = float(input())
mean = float(input())
sigma = float(input())
middleDistPercentage = float(input())
z = float(input())

cd = cumulativeDist(sampleValues, sigma, z)
print(round(mean - cd, 2))
print(round(mean + cd, 2))