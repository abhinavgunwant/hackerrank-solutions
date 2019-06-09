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
F = list(map(int, input().split()))
S = []

n_ = 0

for i in range(n):
    for j in range(F[i]):
        S.append(X[i])
        n_ += 1        

S.sort()

q1 = calcMedian(S, 0, n_//2 - 1)

if n_ % 2 == 0:
    q3 = calcMedian(S, n_//2, n_-1)
else:
    q3 = calcMedian(S, n_//2 + 1, n_-1)

print(round(float(q3 - q1), 2))