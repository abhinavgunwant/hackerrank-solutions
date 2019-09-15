import math

def cumulativeDist(x, mean, sigma):
    return ( 1.0 + math.erf( (x - mean) / (sigma * math.sqrt(2)) ) ) / 2.0

mean, sigma = list(map(float, input().split()))
firstQues = float(input())
secondQuesRange = list(map(float, input().split()))

print(round(cumulativeDist(firstQues, mean, sigma), 3))
print(round((cumulativeDist(secondQuesRange[1], mean, sigma) - cumulativeDist(secondQuesRange[0], mean, sigma)), 3))