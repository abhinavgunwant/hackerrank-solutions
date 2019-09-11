import math

def cumulativeDist(x, mean, sigma):
    return ( 1.0 + math.erf( (x - mean) / (sigma * math.sqrt(2)) ) ) * 0.5

tickets = float(input())
students = float(input())
mean = float(input())
sigma = float(input())

print(round(cumulativeDist(tickets, students * mean,  math.sqrt(students) * sigma), 4))