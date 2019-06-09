#!/bin/python

import sys

def greedy(n):
    temp = n
    db3 = 0
    db5 = 0

    #dividing by 3
    while temp>0:
        if temp-3 >= 0 and temp%5 != 0:
            db3 += 1
            temp -= 3
        elif temp-5 >=0 and temp%3 != 0:
            db5 += 1
            temp -= 5
        else:
            return [-1, -1]

    # print('for n = ' + str(n) + ', no of 3:' + str(db3) + ' and no of 5:' + str(db5))
    return [db3, db5]

def findDecentNo(n):
    db = greedy(n)
    if db[0] == -1:
        sys.stdout.write('-1')
        return
    # digits = n
    str_ = ''
    # temp = digits = n

    #
    # while temp > 0:
    #     if temp-3 >= 0 and temp%5 != 0:
    #         temp -= 3
    #     elif temp-5 >= 0 and tmep%3 != 0:
    #         temp -= 5

    if n%3 == 0:
        while n > 0:
            sys.stdout.write('555')
            n -= 3
        return

    if n%5 == 0:
        while n>0:
            sys.stdout.write('33333')
            n-=5
        return

    # while digits > 0:
    #     if digits-3 >= 0 and digits != 5:# temp%3 == 0):# or temp-3%5 == 0):
    #         digits -= 3
    #         str_ += '555'
    #     elif digits-5 >= 0 and digits != 3:# or temp-5%3 == 0):
    #         digits -= 5
    #         str_ += '33333'
    #     else:
    #         return '-1'


    for i in xrange(db[0]):
        sys.stdout.write('555')


    for i in xrange(db[1]):
        sys.stdout.write('33333')

    return


inputs = []
t = int(raw_input().strip())
for a0 in xrange(t):
    inputs.append(int(raw_input().strip()))

# len_ = len(inputs)
for i in inputs:
    findDecentNo(i)
    sys.stdout.write('\n')
