#!/bin/python3

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

fine = 0

aDay, aMonth, aYear = map(int, input().split())
eDay, eMonth, eYear = map(int, input().split())

if aYear > eYear:
    fine = 10000
elif aMonth > eMonth and aYear == eYear:
    fine = 500 * (aMonth - eMonth)
elif aDay > eDay and aMonth == eMonth and aYear == eYear:
    fine = 15 * (aDay - eDay)

print(fine)