#!/bin/python3

if __name__ == '__main__':
    N = int(input())

    if N % 2 == 1:
        print('Weird')
    else:
        if N >= 2 and N <= 5:
            print('Not Weird')
        elif N >= 6 and N <= 20:
            print('Weird')
        else:
            print('Not Weird')