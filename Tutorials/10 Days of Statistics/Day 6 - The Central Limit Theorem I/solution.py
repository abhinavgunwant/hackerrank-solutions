import math

def cumulativeDist(x, mean, sigma):
    return ( 1.0 + math.erf( (x - mean) / (sigma * math.sqrt(2)) ) ) * 0.5

maxWeight = float(input())
boxes = float(input())
mean = float(input())
sigma = float(input())

print(round(cumulativeDist(maxWeight, boxes * mean,  math.sqrt(boxes) * sigma), 4))