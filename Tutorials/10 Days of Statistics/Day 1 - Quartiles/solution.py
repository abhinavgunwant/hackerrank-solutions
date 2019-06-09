# Function to calculate median
def calcMedian(arr, startIndex, endIndex):
    index = ( startIndex + endIndex ) // 2
    if (endIndex - startIndex + 1) % 2 == 0:
        # return median for even no of elements
        return ( arr[index] + arr[index + 1] ) // 2
    else:
        # return median for odd no of elements
        return arr[index]

# Get n
n = int(input())

# Get list array X
X = list(map(int, input().split()))
X.sort()

q1 = calcMedian(X, 0, n//2 - 1)
q2 = calcMedian(X, 0, n-1)

if n % 2 == 0:
    q3 = calcMedian(X, n//2, n-1)
else:
    q3 = calcMedian(X, n//2 + 1, n-1)

# Print result
print(q1)
print(q2)
print(q3)