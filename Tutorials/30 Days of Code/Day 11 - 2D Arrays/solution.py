#!/bin/python3

import math

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    maxSum = - math.inf

    for i in range(6):
        for j in range(6):
            if i < 4 and j < 4:
                sum_ = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
                    + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

                if sum_ > maxSum:
                    maxSum = sum_
    
    print(maxSum)
    