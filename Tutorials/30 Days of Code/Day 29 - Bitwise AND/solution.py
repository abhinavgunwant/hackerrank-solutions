#!/bin/python3

#### Note: Go through the problem statement!

# for explanations, see the following threads in
# the hackerrank forum:
# https://www.hackerrank.com/challenges/30-bitwise-and/forum/comments/163404
# https://www.hackerrank.com/challenges/30-bitwise-and/forum/comments/307234

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, k = map(int, input().split())

        if (k - 1) | k <= n:
            print(k-1)
        else:
            print(k-2)