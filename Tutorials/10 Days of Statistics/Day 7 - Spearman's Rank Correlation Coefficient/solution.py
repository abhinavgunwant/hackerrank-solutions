# Based on the explanation in the explanation of the
# sample input case (i.e. assuming that the input
# values are all unique!)

## calculates rank vector for a list 'l'
def rank(l):
    lSetList = list(set(l))
    lSetList.sort()

    last = -float('inf')
    rankDict = {}
    currentRank = 0

    for i in lSetList:
        currentRank += 1
        last = i
        rankDict[i] = currentRank
    
    rankList = []

    for i in l:
        rankList.append(rankDict[i])

    return rankList

## calculates sum of square of difference of ranks
def DiffRankSum(X, Y, n):
    xRank = rank(X)
    yRank = rank(Y)

    diffList = []

    for i in range(n):
        diffList.append((xRank[i] - yRank[i]) ** 2)

    return sum(diffList)

def spearmanRankCoeff(X, Y, n):
    return 1 - ( ( 6 * DiffRankSum(X, Y, n) ) / (n * ( n**2 - 1) ) )

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print(round(spearmanRankCoeff(X, Y, n), 3))