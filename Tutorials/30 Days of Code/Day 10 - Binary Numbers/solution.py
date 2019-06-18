#!/bin/python3

# solution based on tutorial, check out solution2.py too
# for an more pythonic solution!

if __name__ == '__main__':
    n = int(input())

    binStr = '' # string denoting binary no

    while n > 0:
        if n % 2 == 1:
            binStr = '1' + binStr
        else:
            binStr = '0' + binStr

        n //= 2
    

    found1 = False
    consec1 = 0
    maxConsec1 = 0
    binStrLen = len(binStr)

    for i in range(binStrLen):
        if binStr[i] == '1':
            if found1:
                consec1 += 1
            else:
                consec1 = 1
                found1 = True
        else:
            found1 = False

        if consec1 > maxConsec1:
            maxConsec1 = consec1

    print(maxConsec1)