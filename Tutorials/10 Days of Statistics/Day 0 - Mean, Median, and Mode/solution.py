# TODO: make different functions...

n = int(input())

# Get the Array 'X'
xArr = list(map(int, input().split()))

#---- Calculate mean ----
mean = sum(xArr) / len(xArr)

# Sort X (to help in median calculation)
xArr.sort()

#---- Calculate Median ----
median = 0
if len(xArr)%2 == 0:
    # When the no. of elements in array is even, the
    # median is the mean of the two middle elements.
    # Note: a // b is the "floor division" which returns
    # integer
    median = (xArr[ len(xArr)//2 - 1 ] + xArr[ len(xArr)//2 + 1]) / 2
else:
    median = xArr[ len(xArr)//2 ]

print(mean)
print(median)
print(stats.mode(X).mode[0])