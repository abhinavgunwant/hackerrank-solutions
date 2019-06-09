
# function to multiply corresponding elements of two arrays
def multiply(A, B):
    res = []
    for i in range(len(A)):
        res.append(A[i] * B[i])    
    return res

n = int(input())

# get all the elements for array X
X = list(map(int, input().split()))

# get all the weights corresponding to each element in X
W = list(map(int, input().split()))

# calculate the weighted mean
Mw = round( sum( multiply(X,W) ) / sum(W), 1 )

print(Mw)