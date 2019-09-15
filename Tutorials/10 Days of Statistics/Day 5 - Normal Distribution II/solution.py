import math

def cumulativeDist(x, mean, sigma):
    return ( 1 + math.erf( (x - mean) / (sigma * math.sqrt(2)) ) ) / 2

mean, sigma = list(map(float, input().split()))
firstQues = float(input())
secondQues = float(input())

print(round(( 1 - cumulativeDist(firstQues, mean, sigma) ) * 100, 2))
print(round(( 1 - cumulativeDist(secondQues, mean, sigma) ) * 100, 2))
print(round(cumulativeDist(secondQues, mean, sigma) * 100, 2))