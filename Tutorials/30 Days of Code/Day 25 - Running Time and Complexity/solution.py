#!/bin/python3

import math

def isPrime(num):
    if num == 2:
        return True

    if num % 2 == 0 or num == 1:
        return False

    #### Check if number is divisible by 3 to square
    #### root of of itself
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    return True

t = int(input())

numbers = []

for i in range(t):
    number = int(input())
    numbers.append(number)

for number in numbers:
    if isPrime(number):
        print('Prime')
    else:
        print('Not prime')
