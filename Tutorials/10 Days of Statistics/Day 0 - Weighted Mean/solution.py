def multiply(A, B):
    res = []
    for i in range(len(A)):
        res.append(A[i] * B[i])    
    return res


n = int(input())

A = list(map(int, input().split()))
W = list(map(int, input().split()))

print(round(sum(multiply(A,W))/sum(W), 1))