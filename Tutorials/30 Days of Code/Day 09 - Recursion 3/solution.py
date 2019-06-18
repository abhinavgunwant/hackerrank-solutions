#!/bin/python3

phoneBook = dict()

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        name, phone = input().split()
        phoneBook[name] = phone


    try:
        while True:
            query = input()

            if query in phoneBook:
                print(query + '=' + phoneBook[query])
            else:
                print('Not found')
    except EOFError:
        exit()